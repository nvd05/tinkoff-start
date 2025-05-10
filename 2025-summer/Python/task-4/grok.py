
from bisect import bisect_right


def solve():
	# Чтение входных данных
	n = int(input())
	A = list(map(int, input().split()))

	# Создаем списки позиций для каждого числа от 1 до 10
	positions = [[] for _ in range(11)]
	for i in range(n):
		positions[A[i]].append(i + 1)  # Индексы с 1

	# Инициализация M_r
	M_prev = 0  # M_{r-1}, начальное значение для r=3
	result = 0

	# Перебираем правый конец r от 3 до n
	for r in range(3, n + 1):
		max_new = 0  # Максимальный i для новых троек с k=r
		# Перебираем j от 1 до r-1
		for j in range(1, r):
			x = 2 * A[j - 1] - A[r - 1]  # A_i = 2A_j - A_r
			if 1 <= x <= 10:
				# Находим последний i < j, где A_i = x
				idx = bisect_right(positions[x], j - 1) - 1
				if idx >= 0 and positions[x][idx] < j:
					max_new = max(max_new, positions[x][idx])

		# Обновляем M_r
		M_r = max(M_prev, max_new)
		result += M_r
		M_prev = M_r

	print(result)


if __name__ == "__main__":
	solve()
