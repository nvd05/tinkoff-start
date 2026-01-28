
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
