
def task_5(n: int, m: int, v: list[int], h: list[int]) -> int:
	if n == 1 and m == 1:
		return 0
	sum_v = sum(v[:n-1])
	sum_h = sum(h[:m-1])
	min_v = min(v[:n-1]) if n > 1 else 0
	min_h = min(h[:m-1]) if m > 1 else 0
	if n == 1:
		return sum_h
	if m == 1:
		return sum_v
	return min(sum_v + min_h, sum_h + min_v)

if __name__ == "__main__":
	n, m = list(map(int, input().split()))

	# Чтение стоимостей вертикальных дорог V
	v_costs = list(map(int, input().split()))

	# Чтение стоимостей горизонтальных дорог H
	h_costs = list(map(int, input().split()))

	res = task_5(n, m, v_costs, h_costs)
	print(res)
