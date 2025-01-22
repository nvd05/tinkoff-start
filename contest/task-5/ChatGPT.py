
def count_uniform_numbers(a, b):
	count = 0
	for d in range(1, 10):  # Цифры от 1 до 9
		num = d
		while num <= b:  # Пока число не превышает верхнюю границу
			if a <= num <= b:  # Если число в диапазоне [a, b]
				count += 1
			num = num * 10 + d  # Переходим к числу с еще одной одинаковой цифрой
	return count

# Чтение входных данных
a, b = map(int, input().split())

# Вывод результата
print(count_uniform_numbers(a, b))
