
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

	for (const section of ['Вопрос', 'Формат входных данных', 'Формат выходных данных', 'Примечания', 'Примеры данных'])
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

	return lines.join('\n');
}
