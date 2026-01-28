
MOD = 10**9 + 7

def task_7(n, k):
	# Построение списков длин диагоналей для белых и черных клеток
	white_diags = []
	black_diags = []
	for s in range(2 * n - 1):  # s = i+j, от 0 до 2n-2
		low = max(0, s - (n - 1))
		high = min(n - 1, s)
		length = high - low + 1
		if s % 2 == 0:
			white_diags.append(length)
		else:
			black_diags.append(length)
	
	# Сортируем оба списка
	white_diags.sort()
	black_diags.sort()
	
	# Функция для вычисления dp для данного списка длин диагоналей
	def compute_dp(diags, max_k):
		dp = [0] * (max_k + 1)
		dp[0] = 1
		for L in diags:
			# Обновляем с конца, чтобы не использовать обновленные значения в той же диагонали
			for j in range(max_k, 0, -1):
				# Количество способов добавить слона на текущую диагональ
				ways = max(0, L - (j - 1))
				dp[j] = (dp[j] + dp[j - 1] * ways) % MOD
		return dp
	
	# Максимальное количество слонов, которое можно разместить на каждом цвете
	max_white = min(k, len(white_diags))
	max_black = min(k, len(black_diags))
	
	dp_white = compute_dp(white_diags, max_white)
	dp_black = compute_dp(black_diags, max_black)
	
	# Суммирование
	ans = 0
	for i in range(max_white + 1):
		if k - i <= max_black:
			ans = (ans + dp_white[i] * dp_black[k - i]) % MOD
	
	return ans

if __name__ == "__main__":
	input_data = input().strip().split()
	n, k = map(int, input_data)
	print(task_7(n, k))
