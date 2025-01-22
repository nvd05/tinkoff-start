
def is_prime(n):
	"""
	Проверяет, является ли число простым.
	"""

	if n <= 1:
		return False

	for i in range(2, int(n*0.5) + 1):
		if n % i == 0:
			return False

	return True

def count_composite_with_prime_divisors(l, r):
	"""
	Считает количество составных чисел от l до r, имеющих простое количество делителей.
	"""

	count = 0

	for num in range(l, r + 1):
		if not is_prime(num) and is_prime(sum(1 for i in range(1, num + 1) if num % i == 0)):
			count += 1

	return count

# Считываем входные данные
l, r = map(int, input().split())

# Вычисляем и выводим результат
result = count_composite_with_prime_divisors(l, r)
print(result)
