
window.tinkoff_practice = new class TinkoffPractice
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
			.replace(/\s*\\times\s*/g, ' * ');
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
