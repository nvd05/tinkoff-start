
const sections = [
	{
		regex: /Предыдущие решения(.*)$/s,
		title: 'Предыдущие решения',
	},
	{
		regex: /Решение(.*)$/s,
		title: 'Решение',
	},
	{
		regex: /Примеры данных(.*)$/s,
		title: 'Примеры данных',
	},
	{
		regex: /Замечани[е|я](.*)$/s,
		title: 'Примечания',
	},
	{
		regex: /Формат выходных данных(.*)$/s,
		title: 'Формат выходных данных',
	},
	{
		regex: /Формат входных данных(.*)$/s,
		title: 'Формат входных данных',
	},
	{
		regex: /МБ(.*)$/s,
		title: 'Вопрос',
	},
	{
		regex: /Ограничение памяти\s*(\d*)/,
		title: 'Ограничение памяти',
	},
	{
		regex: /Ограничение времени\s*(\d*\sсекунда)/,
		title: 'Ограничение времени',
	},
	{
		regex: /(\d*)\s*баллов/,
		title: 'Балл',
	},
	{
		regex: /(\d*)\s*задание/,
		title: 'Задание',
	},
];

function getSections (text)
{
	const responses = {
		unprocessed: null
	};

	for (const section of sections)
	{
		const response = section.regex.exec(text);

		if (!response)
		{
			continue;
		}

		responses[section.title] = response[1].trim();
		text = text.substring(0, response.index).trim();
	}

	responses.unprocessed = text;

	return responses;
}
