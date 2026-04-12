
def task_5(n: int, m: int, v: list[int], h: list[int]) -> int:
	# Минимальное расстояние
	dist = (n - 1) + (m - 1)

	# 1. Считаем базовый кратчайший путь
	# Можно либо пройти через лучшую строку i, либо через лучший столбец j

	# Вариант А: идем по столбцу 1 до строки i, там всю горизонталь, потом по столбцу M до конца
	# Стоимость = (i-1)*H[0] + (m-1)*V[i-1] + (n-i)*H[m-1]
	res_v = float('inf')
	for i in range(1, n + 1):
		cost = (i - 1) * h[0] + (m - 1) * v[i - 1] + (n - i) * h[m - 1]
		if cost < res_v:
			res_v = cost

	# Вариант Б: идем по строке 1 до столбца j, там всю вертикаль, потом по строке N до конца
	# Стоимость = (j-1)*V[0] + (n-1)*H[j-1] + (m-j)*V[n-1]
	res_h = float('inf')
	for j in range(1, m + 1):
		cost = (j - 1) * v[0] + (n - 1) * h[j - 1] + (m - j) * v[n - 1]
		if cost < res_h:
			res_h = cost

	min_base = min(res_v, res_h)

	return min_base

if __name__ == "__main__":
	n, m = list(map(int, input().split()))

	# Чтение стоимостей вертикальных дорог V
	v_costs = list(map(int, input().split()))

	# Чтение стоимостей горизонтальных дорог H
	h_costs = list(map(int, input().split()))

	res = task_5(n, m, v_costs, h_costs)
	print(res)
