
# tinkoff start

> Попытки решить задачи вступительного экзамена на стажировку Тинькофф Старт.

+ это попытки решить задачи собственными силами.
+ сборник ссылок на другие репозитории решений.
+ предпочитаемый язык: Python 3.8

| сезон           | задач | баллов    | %     |
|-----------------|-------|-----------|-------|
| осень 2024      | 4 / 6 | 105 / 600 | 17.5  |
| лето 2025       | 6 / 7 | 338 / 700 | 48.29 |
| зима-весна 2025 | 7 / 7 | 304 / 700 | 43.43 |

## Скопировать текст задания

+ Автоматический скрипт|расширение: `Tampermonkey.js`.
+ Ручное копирование содержимого:

```javascript
window.tinkoff_task = new class TinkoffTask
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
		for (const tag_paragraph of cloned.querySelectorAll('p'))
		{
			tag_paragraph.textContent += '\n';
		}

		return cloned.textContent;
	}

	copyToClipboard (text)
	{
		const tag_textarea = document.createElement('textarea');
		tag_textarea.value = text;

		document.body.appendChild(tag_textarea);
		tag_textarea.select();

		const status = document.execCommand('copy');
		tag_textarea.remove();

		return status;
	}

	constructor ()
	{
		this.has_copied = this.copyToClipboard(this.text);

		this.message = this.has_copied
			? 'COPIED'
			: 'FAILED TO SEND TO CLIPBOARD';

		console.debug(this.message);
	}
};
```
