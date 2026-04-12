
def task_5(n: int, m: int, v: list[int], h: list[int]) -> int:
	if n == 1 and m == 1:
		return 0

	# Построение нижней выпуклой оболочки для точек (j, h[j])
	# j - координата x (от 0 до m-1), h[j] - координата y
	hull = []
	for j in range(m):
		while len(hull) >= 2:
			j1, j2 = hull[-2], hull[-1]
			# Проверка поворота (векторное произведение) для выпуклости
			if (h[j2] - h[j1]) * (j - j2) >= (h[j] - h[j2]) * (j2 - j1):
				hull.pop()
			else:
				break
		hull.append(j)

	def get_slope_cmp(idx, i_val):
		"""Сравнение наклона ребра оболочки с целевым наклоном."""
		j1, j2 = hull[idx], hull[idx+1]
		# Условие: slope(j1, j2) >= (v[i] - v[0]) / i
		return (h[j2] - h[j1]) * i_val >= (v[i_val] - v[0]) * (j2 - j1)

	min_total_cost = float('inf')

	# Перебираем все возможные "магистральные" строки i
	for i in range(n):
		if i == 0:
			# Путь по границам: (1,1) -> (1,m) -> (n,m)
			current_cost = (m - 1) * v[0] + (n - 1) * h[m - 1]
		else:
			# Ищем оптимальный столбец j на выпуклой оболочке бинарным поиском
			low = 0
			high = len(hull) - 2
			best_idx = len(hull) - 1

			while low <= high:
				mid = (low + high) // 2
				if get_slope_cmp(mid, i):
					best_idx = mid
					high = mid - 1
				else:
					low = mid + 1

			j_opt = hull[best_idx]
			# Вычисление стоимости по формуле (используем 0-индексацию)
			current_cost = (j_opt * v[0] +
							(m - 1 - j_opt) * v[i] +
							i * h[j_opt] +
							(n - 1 - i) * h[m - 1])

		if current_cost < min_total_cost:
			min_total_cost = current_cost

	return int(min_total_cost)

if __name__ == "__main__":
	n, m = list(map(int, input().split()))

	# Чтение стоимостей вертикальных дорог V
	v_costs = list(map(int, input().split()))

	# Чтение стоимостей горизонтальных дорог H
	h_costs = list(map(int, input().split()))

	res = task_5(n, m, v_costs, h_costs)
	print(res)
