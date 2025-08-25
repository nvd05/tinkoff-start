"""
DeepSeek
"""


def task_1(number: str) -> str:
	digits = sorted(number)

	zeros = []
	non_zeros = []

	for char in digits:
		if char == '0':
			zeros.append(char)
		else:
			non_zeros.append(char)

	# Формируем результат: первая цифра - первая ненулевая, затем все нули, затем остальные ненулевые
	result = non_zeros[0] + ''.join(zeros) + ''.join(non_zeros[1:])
	return result

if __name__ == '__main__':
	number = input()
	response = task_1(number)
	print(response)
