
def task_3(n: int, m: int, refs: list[list[int]]) -> list[str]:
	res = []

	for ref in refs:
		u, v = ref

		# Направляем от меньшего к большему
		if u < v:
			res.append(f"{u} {v}")
		else:
			res.append(f"{v} {u}")

	return res

if __name__ == "__main__":
	n, m = list(map(int, input().split()))
	refs = [list(map(int, input().split())) for _ in range(m)]

	res = task_3(n, m, refs)
	print('\n'.join(res))
