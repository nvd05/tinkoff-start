
def task_5(tasks: int, parents: list[int], awards: list[int]) -> bool:
	if tasks < 3:
		return False

	total_sum = sum(awards)
	if total_sum % 3 != 0:
		return False

	target = total_sum // 3

	# ===== ===== ===== ===== =====
	# dependencies
	# ===== ===== ===== ===== =====

	children = [[] for _ in range(tasks + 1)]
	root = None
	for i in range(1, tasks + 1):
		parent = parents[i - 1]

		if parent == 0:
			root = i
			continue

		children[parent].append(i)

	# ===== ===== ===== ===== =====
	# queue
	# ===== ===== ===== ===== =====

	order = []
	stack = [root]
	while stack:
		u = stack.pop()
		order.append(u)
		for v in children[u]:
			stack.append(v)
	order.reverse()

	# ===== ===== ===== ===== =====
	# awards
	# ===== ===== ===== ===== =====

	sum_tree = [0] * (tasks + 1)
	for i in range(1, tasks + 1):
		sum_tree[i] = awards[i - 1]

	# ===== ===== ===== ===== =====
	# logics
	# ===== ===== ===== ===== =====

	has_target = [False] * (tasks + 1)
	found = False

	for u in order:
		for v in children[u]:
			sum_tree[u] += sum_tree[v]

		count = 0
		for v in children[u]:
			if has_target[v]:
				count += 1

		if count >= 2:
			found = True
			break

		if count >= 1 and sum_tree[u] == target and u != root:
			found = True
			break

		if sum_tree[u] == 2 * target and count >= 1 and u != root:
			found = True
			break

		has_target[u] = (sum_tree[u] == target) or (count > 0)

	return found

if __name__ == '__main__':
	tasks = int(input())
	parents = [int(value) for value in input().split(' ')]
	awards = [int(value) for value in input().split(' ')]

	status = task_5(tasks, parents, awards)
	print('YES' if status else 'NO')
