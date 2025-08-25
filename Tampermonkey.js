// ==UserScript==
// @name         Tinkoff Education Task Copier
// @namespace    http://tampermonkey.net/
// @version      1.1
// @description  Копирует содержимое задания с Tinkoff Education в формате Markdown
// @author       https://github.com/nvd05
// @match        https://edu.tbank.ru/selection/*/practice/*/task/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tbank.ru
// @grant        none
// ==/UserScript==

// #region practice

class TinkoffHeader
{
	/** @param {HTMLDivElement} tag_header */
	constructor(tag_header)
	{
		this.tag_header = tag_header;

		this.tag_title = tag_header.querySelector('.tui-text_body-xl');
		this.tag_points = tag_header.querySelector('tui-badge[data-appearance="info"]');

		this.title = this.tag_title?.textContent.trim();
		this.points = this.tag_points?.textContent.trim();
	}
}

class TinkoffLimits
{
	/** @param {HTMLElement} tag_limits */
	constructor(tag_limits)
	{
		this.tag_limits = tag_limits;
	}

	serializeToJSON ()
	{
		const items = [...this.tag_limits.querySelectorAll('.item')];

		return items.map(item => ({
			title: item.querySelector('.title').textContent.trim(),
			value: item.querySelector('.description').textContent.trim()
		}));
	}
}

class TinkoffQuestion
{
	/** @param {HTMLElement} tag_question */
	constructor(tag_question)
	{
		this.tag_question = tag_question;
		this.tag_editor = tag_question.querySelector('.ql-editor');

		/** @type { { title: string, getText ?: (text: string) => string }[] } */
		this.sections = [
			{
				title: 'Вопрос',

				getText (text)
				{
					return text;
				}
			},
			{
				title: 'Формат входных данных',
			},
			{
				title: 'Формат выходных данных',
			},
			{
				title: 'Замечание',
			},
		];

		this.parser = new DOMParser();
	}

	get html ()
	{
		const tagClone = this.parser.parseFromString(this.tag_editor.innerHTML, 'text/html').body;

		// Заменить формулы на обычный текст
		tagClone.querySelectorAll('span.ql-formula').forEach(formula =>
		{
			formula.replaceWith(document.createTextNode(formula.getAttribute('data-value')));
		});

		// Добавить переносы строк
		tagClone.querySelectorAll('p, div').forEach(el =>
		{
			el.innerHTML += '\n\n';
		});

		const text = tagClone.innerText
			.replaceAll(/\s*\\times\s*/g, ' * ')
			.replaceAll(/\s*\\leq\s*/g, ' <= ');

		return text;
	}

	splitSections (content)
	{
		const original = content;
		let modified = content;

		const response = {};

		for (let i = this.sections.length - 1; i >= 0; i--)
		{
			const section = this.sections[i];

			if (section.getText)
			{
				response[section.title] = section.getText(modified).trim();
				continue;
			}

			const index = modified.lastIndexOf(section.title);

			if (index === -1)
			{
				continue;
			}

			response[section.title] = modified.substring(index + section.title.length).trim();
			modified = modified.substring(0, index).trim();
		}

		return {
			original: original,
			sections: response
		};
	}

	serializeToJSON ()
	{
		return this.splitSections(this.html);
	}
}

class TinkoffExamples
{
	/** @param {HTMLElement} tag_examples */
	constructor(tag_examples)
	{
		this.tag_examples = tag_examples;
	}

	serializeToJSON ()
	{
		/** @type {HTMLDivElement[]} */
		const titles = [...this.tag_examples.querySelectorAll('div.subtitle')];

		return titles.map(function (tag_title)
		{
			const title = tag_title.textContent.trim();

			const tag_example = tag_title.nextElementSibling;

			const tag_input = tag_example.firstElementChild.querySelector('textarea');
			const tag_output = tag_example.lastElementChild.querySelector('textarea');

			return {
				title,
				input: tag_input.value.trim(),
				output: tag_output.value.trim()
			};
		});
	}
}

class TinkoffTask
{
	/** @param {HTMLElement} tag_task */
	constructor(tag_task)
	{
		this.tag_task = tag_task;

		this.tag_header = tag_task.querySelector('div.header-task');
		this.tag_limits = tag_task.querySelector('app-limitation-program-task');
		this.tag_question = tag_task.querySelector('app-quill-content-display');
		this.tag_examples = tag_task.querySelector('app-samples-program-task');

		this.header = this.tag_header instanceof HTMLDivElement
			? new TinkoffHeader(this.tag_header)
			: null;

		this.question = this.tag_question instanceof HTMLElement
			? new TinkoffQuestion(this.tag_question)
			: null;

		this.limits = this.tag_limits instanceof HTMLElement
			? new TinkoffLimits(this.tag_limits)
			: null;

		this.examples = this.tag_examples instanceof HTMLElement
			? new TinkoffExamples(this.tag_examples)
			: null;
	}
}

// #endregion practice
// ===== ===== ===== ===== =====
// #region practice ui

/** @param {TinkoffTask} task */
function convertToMarkdown (task)
{
	let response = '';

	const title = [task.header.title, task.header.points].join(' | ');
	response += `# ${title}\n\n`;

	const limits = task.limits?.serializeToJSON();
	if (limits)
	{
		response += `## Ограничения\n\n`;

		for (const limit of limits)
		{
			response += `+ ${limit.title}: ${limit.value}\n`;
		}

		response += '\n';
	}

	const question = task.question?.serializeToJSON();
	if (question)
	{
		for (const section of task.question.sections)
		{
			const data = question.sections[section.title];

			if (data)
			{
				response += `## ${section.title}\n\n${data}\n\n`;
			}
		}
	}

	const examples = task.examples?.serializeToJSON();
	if (examples)
	{
		response += '## Примеры данных\n\n';

		for (const example of examples)
		{
			response += `### ${example.title}\n\n`;
			response += `Вход:\n\n\`\`\`\n${example.input}\n\`\`\`\n\n`;
			response += `Выход:\n\n\`\`\`\n${example.output}\n\`\`\`\n\n`;
		}
	}

	return response.trim();
}

class TinkoffUI
{
	/** @param {TinkoffTask} task */
	constructor(task)
	{
		this.task = task;

		this.tag_icon = this.getImportButton();
		task.tag_header?.prepend(this.tag_icon);
	}

	getImportButton ()
	{
		const button = document.createElement('button');
		button.innerHTML = '📋 Копировать задание';
		button.style.cssText = `
			margin-left: 15px;
			padding: 6px 12px;
			background: #0d6efd;
			color: white;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-family: inherit;
			font-size: 14px;
		`;

		button.addEventListener('click', () =>
		{
			const markdown = convertToMarkdown(this.task);

			if (this.copyToClipboard(markdown))
			{
				this.showNotification('Задание скопировано в буфер обмена!', '#0d6efd');
				console.debug('COPIED');
			}
			else
			{
				this.showNotification('Не удалось скопировать в буфер обмена', '#FD4D4D');
				console.error('FAILED TO SEND TO CLIPBOARD');
			}
		});

		return button;
	}

	copyToClipboard (text)
	{
		const textarea = document.createElement('textarea');
		textarea.value = text;
		document.body.appendChild(textarea);
		textarea.select();

		const status = document.execCommand('copy');
		document.body.removeChild(textarea);

		return status;
	}

	showNotification (message, status)
	{
		const notification = document.createElement('div');
		notification.textContent = message;
		notification.style.cssText = `
			position: fixed;
			top: 20px;
			right: 20px;
			padding: 15px;
			background: ${status};
			color: white;
			border-radius: 4px;
			z-index: 9999;
			box-shadow: 0 2px 10px rgba(0,0,0,0.2);
			font-family: sans-serif;
		`;

		document.body.appendChild(notification);
		setTimeout(() =>
		{
			document.body.removeChild(notification);
		}, 3000);
	}
}

function initializePractice ()
{
	const tag_task = document.querySelector('app-practice-task');

	if (tag_task instanceof HTMLElement)
	{
		const task = new TinkoffTask(tag_task);
		const ui = new TinkoffUI(task);

		return ui;
	}

	return null;
}

// #endregion practice ui

function initialize ()
{
	const handler = initializePractice();

	if (handler)
	{
		console.debug('tinkoff_education_extension', handler);
		window.tinkoff_education_extension = handler;
		return;
	}

	console.debug('tinkoff_education_extension', 're-initialize in 1 second');
	setTimeout(initialize, 1_000);
}

window.addEventListener('load', initialize);
