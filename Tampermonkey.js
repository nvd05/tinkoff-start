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

class TinkoffParser
{
	constructor()
	{
		this.task = this.getTaskElement();
		this.title = this.getTaskTitle();
		this.points = this.getTaskPoints();
		this.limits = new TinkoffLimits(this.task);
		this.question = new TinkoffQuestion(this.task);
		this.examples = new TinkoffExamples(this.task);
	}

	getTaskElement ()
	{
		return document.querySelector('app-practice-task');
	}

	getTaskTitle ()
	{
		const titleEl = this.task.querySelector('.header-task .tui-text_body-xl');
		return titleEl ? titleEl.textContent.trim() : 'Задание';
	}

	getTaskPoints ()
	{
		const badge = this.task.querySelector('tui-badge[data-appearance="info"]');
		return badge ? badge.textContent.trim() : '';
	}
}

class TinkoffLimits
{
	constructor(task)
	{
		this.task = task;
		this.tag = task.querySelector('app-limitation-program-task');
	}

	parse ()
	{
		if (!this.tag)
		{
			return '';
		}

		const items = this.tag.querySelectorAll('.item');
		const limits = [];

		items.forEach(item =>
		{
			const title = item.querySelector('.title').textContent.trim();
			const value = item.querySelector('.description').textContent.trim();
			limits.push(`+ ${title}: ${value}`);
		});

		return limits.join('\n');
	}
}

class TinkoffQuestion
{
	constructor(task)
	{
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
		this.task = task;
		this.tag = task.querySelector('app-quill-content-display');
		this.editor = this.tag?.querySelector('.ql-editor');
	}

	parse ()
	{
		if (!this.editor)
		{
			return {
				content: '',
				sections: {}
			};
		}

		const tagClone = this.parser.parseFromString(this.editor.innerHTML, 'text/html').body;

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

		return this.splitSections(text);
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
}

class TinkoffExamples
{
	constructor(task)
	{
		this.task = task;
		this.tag = task.querySelector('app-samples-program-task');
	}

	parse ()
	{
		if (!this.tag)
		{
			return [];
		}

		const examples = [];
		const exampleSections = this.tag.querySelectorAll('.subtitle.ng-star-inserted');

		exampleSections.forEach(section =>
		{
			const title = section.textContent.trim();
			const container = section.nextElementSibling;

			if (container)
			{
				const inputArea = container.querySelector('.sample-field:first-child textarea');
				const outputArea = container.querySelector('.sample-field:last-child textarea');

				if (inputArea && outputArea)
				{
					examples.push({
						title,
						input: inputArea.value.trim(),
						output: outputArea.value.trim()
					});
				}
			}
		});

		return examples;
	}
}

class MarkdownFormatter
{
	constructor(parser)
	{
		this.parser = parser;
	}

	format ()
	{
		const title = `# ${this.parser.title} ${this.parser.points ? `(${this.parser.points})` : ''}`;
		const limits = this.parser.limits.parse();
		const question = this.parser.question.parse();
		const examples = this.parser.examples.parse();

		let md = `${title}\n\n`;

		if (limits)
		{
			md += `## Ограничения\n\n${limits}\n\n`;
		}

		// Добавляем секции
		const sections = [
			{ title: 'Вопрос', key: 'Вопрос' },
			{ title: 'Формат входных данных', key: 'Формат входных данных' },
			{ title: 'Формат выходных данных', key: 'Формат выходных данных' },
			{ title: 'Замечание', key: 'Замечание' }
		];

		sections.forEach(section =>
		{
			if (question.sections[section.key])
			{
				md += `## ${section.title}\n\n${question.sections[section.key]}\n\n`;
			}
		});

		if (examples.length > 0)
		{
			md += `## Примеры данных\n\n`;
			examples.forEach((ex, i) =>
			{
				md += `### Пример ${i + 1}\n\n`;
				md += `Вход:\n\n\`\`\`\n${ex.input}\n\`\`\`\n\n`;
				md += `Выход:\n\n\`\`\`\n${ex.output}\n\`\`\`\n\n`;
			});
		}

		return md.trim();
	}
}

class TinkoffUI
{
	constructor()
	{
		this.parser = null;
		this.init();
	}

	init ()
	{
		try
		{
			this.parser = new TinkoffParser();
			this.addCopyButton();
		}
		catch (error)
		{
			console.log('Tinkoff Education Copier: waiting for page load...');
			setTimeout(() => this.init(), 1000);
		}
	}

	addCopyButton ()
	{
		const header = this.parser.task.querySelector('.header-task');

		if (!header)
		{
			return;
		}

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
			const formatter = new MarkdownFormatter(this.parser);
			const markdown = formatter.format();

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

		header.appendChild(button);
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

// Инициализация
window.addEventListener('load', () =>
{
	window.tinkoff_education = new TinkoffUI();
});
