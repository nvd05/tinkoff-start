
def task_7(t: int, refs: list[list[int]]) -> list[str]:
	results = []
	phi = (1 + 5**0.5) / 2

	for ref in refs:
		n = ref[0]
		m = ref[1]

		a = min(n, m)
		b = max(n, m)
		k = b - a

		# Проверка формулы Витхоффа
		if a == int(k * phi):
			results.append("second")
		else:
			results.append("first")

	return results

if __name__ == "__main__":
	t = int(input().strip())
	refs = [list(map(int, input().split())) for _ in range(t)]

	res = task_7(t, refs)
	print('\n'.join(res))
