
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
