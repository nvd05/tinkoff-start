
def task_1(input_str: str) -> str:
	'''
	Функция для решения задачи 1.
	'''

	if len(input_str.replace('0', '')) == 0:
		return '0'

	# Сортируем все цифры по возрастанию
	sorted_chars = sorted(input_str)

	# Если первая цифра после сортировки - '0', нужно найти первую ненулевую
	# и поставить ее на первое место
	if sorted_chars[0] == '0':
		# Находим первый ненулевой символ
		for i in range(len(sorted_chars)):
			if sorted_chars[i] != '0':
				# Меняем местами первый ноль и первую ненулевую цифру
				sorted_chars[0], sorted_chars[i] = sorted_chars[i], sorted_chars[0]
				break

	# Объединяем символы в строку
	return ''.join(sorted_chars).lstrip('0')

if __name__ == '__main__':
	s = input().strip()
	print(task_1(s))
