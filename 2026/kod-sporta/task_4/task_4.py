
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def task_4(n: int, k: int) -> int:
	# Количество чисел, делящихся на k
	m0 = n // k
	result = m0 ** 3

	# Если k четное, добавляем тройки с остатком k/2
	if k % 2 == 0:
		half_k = k // 2
		m_half = (n + half_k) // k
		result += m_half ** 3

	return result

if __name__ == '__main__':
	n, k = list(map(int, input().split()))
	res = task_4(n, k)
	print(res)
