"""
DeepSeek
"""


MOD = 10 ** 9 + 7

def task_5(sum: int, pens: int) -> int:
	M = sum + pens  # Максимальный индекс для биномиальных коэффициентов

	# Предвычисление биномиальных коэффициентов C(i, j) для i от 0 до M, j от 0 до i
	C = [[0] * (M + 1) for _ in range(M + 1)]
	for i in range(M + 1):
		C[i][0] = 1
		for j in range(1, i + 1):
			C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD

	# Инициализация динамического программирования
	dp = [0] * (sum + 1)
	dp[0] = 1

	# Перебор всех возможных чисел d от 1 до n
	for d in range(1, sum + 1):
		# Обход сумм s от n до 0 в обратном порядке
		for s in range(sum, -1, -1):
			if dp[s] != 0:
				t = 1
				# Добавление t копий числа d
				while s + d * t <= sum:
					new_s = s + d * t
					# Количество способов раскраски t копий числа d в k цветов
					count_color = C[t + pens - 1][pens - 1]
					dp[new_s] = (dp[new_s] + dp[s] * count_color) % MOD
					t += 1

	return dp[sum] % MOD


if __name__ == '__main__':
	sum, pens = [int(value) for value in input().split()]
	iters = task_5(sum, pens)
	print(iters)
