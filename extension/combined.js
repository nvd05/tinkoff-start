// ===== ===== ===== ===== ===== parser.js ===== ===== ===== ===== =====

class TinkoffPractice
{
	get html ()
	{
		return document.querySelector('app-practice-task').outerHTML;
	}

	get text ()
	{
		const parser = new DOMParser();
		const cloned = parser.parseFromString(this.html, 'text/html').body.firstElementChild;

		// заменить формулы на текст.
		for (const tag_formula of cloned.querySelectorAll('span.ql-formula'))
		{
			tag_formula.textContent = tag_formula.getAttribute('data-value');
		}

		// для удобного просмотра.
		cloned.querySelectorAll('div').forEach(tag_section => tag_section.innerHTML += '\n');
		cloned.querySelectorAll('p').forEach(tag_paragraph => tag_paragraph.innerHTML += '\n\n');

		return cloned.textContent
			.replace(/\u00A0/g, ' ') // Неразрывный пробел
			.replace(/\s*\\leq\s*/g, ' <= ')
			.replace(/\s*\\ne\s*/g, ' != ')
			.replace(/\s*\\to\s*/g, ' => ')
			.replace(/\s*\\times\s*/g, ' * ');
	}
}

function copyToClipboard (text)
{
	const tag_textarea = document.createElement('textarea');
	tag_textarea.value = text;

	document.body.appendChild(tag_textarea);
	tag_textarea.select();

	const status = document.execCommand('copy');
	tag_textarea.remove();

	return status;
}

// ===== ===== ===== ===== ===== sections.js ===== ===== ===== ===== =====

/** @typedef { 'task' | 'points' | 'time_limit' | 'memory_limit' } TinkoffHeaderKeys */
/** @typedef { 'question' | 'input_format' | 'output_format' | 'notes' | 'examples' } TinkoffContentKeys */
/** @typedef { 'solution' | 'history' } TinkoffFooterKeys */
/** @typedef { 'unprocessed' | TinkoffHeaderKeys | TinkoffContentKeys | TinkoffFooterKeys } TinkoffSectionKeys */

/** @type { { regex: RegExp, title: string, key: TinkoffSectionKeys }[] } */
const SECTIONS_TEMPLATE = [
	{
		regex: /Предыдущие решения(.*)$/s,
		title: 'Предыдущие решения',
		key: 'history',
	},
	{
		regex: /Решение(.*)$/s,
		title: 'Решение',
		key: 'solution',
	},
	{
		regex: /Примеры данных(.*)$/s,
		title: 'Примеры данных',
		key: 'examples',
	},
	{
		regex: /Замечани[е|я](.*)$/s,
		title: 'Примечания',
		key: 'notes',
	},
	{
		regex: /Формат выходных данных(.*)$/s,
		title: 'Формат выходных данных',
		key: 'output_format',
	},
	{
		regex: /Формат входных данных(.*)$/s,
		title: 'Формат входных данных',
		key: 'input_format',
	},
	{
		regex: /МБ(.*)$/s,
		title: 'Вопрос',
		key: 'question',
	},
	{
		regex: /Ограничение памяти\s*(\d*)/,
		title: 'Ограничение памяти',
		key: 'memory_limit',
	},
	{
		regex: /Ограничение времени\s*(\d*\sсекунда)/,
		title: 'Ограничение времени',
		key: 'time_limit',
	},
	{
		regex: /(\d*)\s*баллов/,
		title: 'Балл',
		key: 'points',
	},
	{
		regex: /(\d*)\s*задание/,
		title: 'Задание',
		key: 'task',
	},
];

function getSections (text)
{
	/** @type { Partial<Record<TinkoffSectionKeys, Record<'title' | 'value', string>>> } */
	const responses = {};

	for (const section of SECTIONS_TEMPLATE)
	{
		const response = section.regex.exec(text);

		if (!response)
		{
			continue;
		}

		responses[section.key] = {
			title: section.title,
			value: response[1].trim(),
		};

		text = text.substring(0, response.index).trim();
	}

	if (text)
	{
		responses.unprocessed = {
			title: 'Необработанный текст',
			value: text,
		};
	}

	return responses;
}

// ===== ===== ===== ===== ===== markdown.js ===== ===== ===== ===== =====

function getMarkdown (sections)
{
	let lines = [];

	const task = sections['Задание']?.trim();
	const point = sections['Балл']?.trim();
	if (task || point)
	{
		lines.push(`# ${task} задание | ${point} баллов`);
		lines.push('');
	}

	const time_limit = sections['Ограничение времени']?.trim();
	const memory_limit = sections['Ограничение памяти']?.trim();
	if (time_limit || memory_limit)
	{
		lines.push('+ Ограничение времени: ' + time_limit);
		lines.push('+ Ограничение памяти: ' + memory_limit + ' МБ');
		lines.push('');
	}

	for (const section of ['Вопрос', 'Формат входных данных', 'Формат выходных данных', 'Примечания'])
	{
		const data = sections[section]?.trim();

		if (!data)
		{
			continue;
		}

		lines.push('## ' + section);
		lines.push('');
		lines.push(data);
		lines.push('');
	}

	const examples = sections['Примеры данных']?.trim();
	if (typeof examples === 'string')
	{
		lines.push('## Примеры данных');
		lines.push('');

		const array = [...examples.matchAll(/(Пример(\s*)(\d*)(\s*))?Ввод(\s*)([-\d\s\n]*)(\s*)Вывод(\s*)([-\d\s\n]*)/g)];

		if (array.length === 0)
		{
			lines.push('> не удалось обработать по шаблону.');
			lines.push('');
			lines.push(examples);
			lines.push('');
		}

		for (const example of array)
		{
			const title = example[3]?.trim();
			const input = example[6]?.trim();
			const output = example[9]?.trim();

			if (title)
			{
				lines.push('### Пример ' + title);
				lines.push('');
			}

			lines.push('Ввод:');
			lines.push('');
			lines.push('```text');
			lines.push(input);
			lines.push('```');
			lines.push('');

			lines.push('Вывод:');
			lines.push('');
			lines.push('```text');
			lines.push(output);
			lines.push('```');
			lines.push('');
		}
	}

	const unprocessed = sections.unprocessed;
	if (unprocessed)
	{
		lines.push('## Необработанный текст');
		lines.push('');
		lines.push(unprocessed);
		lines.push('');
	}

	return lines.join('\n');
}

// ===== ===== ===== ===== ===== run ===== ===== ===== ===== =====

const tinkoff_practice = new TinkoffPractice();

const sections = getSections(tinkoff_practice.text);
const markdown = getMarkdown(sections);

copyToClipboard(markdown);
