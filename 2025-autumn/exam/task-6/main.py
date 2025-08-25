import collections


def task_6(number_of_vertices: int, number_of_ribs: int, ribs: list[tuple[int, int]]) -> list[tuple[int, int]]:
	edges = []
	adj = [[] for _ in range(number_of_vertices + 1)]
	A = [0] * (number_of_vertices + 1)

	for i in range(number_of_ribs):
		u = int(ribs[i][0])
		v = int(ribs[i][1])
		edges.append((u, v))
		A[u] += 1
		adj[u].append((v, i))
		adj[v].append((u, i))

	if number_of_ribs % 2 != 0:
		return []

	target = [0] * (number_of_vertices + 1)
	for i in range(1, number_of_vertices + 1):
		target[i] = A[i] % 2

	y = [0] * number_of_ribs
	determined = [False] * number_of_ribs
	current_sum = [0] * (number_of_vertices + 1)
	undetermined_sets = [set() for _ in range(number_of_vertices + 1)]

	for u in range(1, number_of_vertices + 1):
		for (v, e) in adj[u]:
			undetermined_sets[u].add(e)

	q = collections.deque()
	for u in range(1, number_of_vertices + 1):
		if len(undetermined_sets[u]) == 1:
			q.append(u)

	while True:
		while q:
			u = q.popleft()
			if not undetermined_sets[u]:
				continue
			e = undetermined_sets[u].pop()
			if determined[e]:
				continue
			u1, v1 = edges[e]
			if u1 == u:
				v = v1
			else:
				v = u1

			y_val = (target[u] - current_sum[u]) % 2
			y[e] = y_val
			determined[e] = True
			current_sum[v] = (current_sum[v] + y_val) % 2
			if e in undetermined_sets[v]:
				undetermined_sets[v].remove(e)
			if len(undetermined_sets[v]) == 1:
				q.append(v)

		found = False
		for u in range(1, number_of_vertices + 1):
			if undetermined_sets[u]:
				found = True
				break
		if not found:
			break
		e = undetermined_sets[u].pop()
		if determined[e]:
			continue
		u1, v1 = edges[e]
		if u1 == u:
			v = v1
		else:
			v = u1
		y_val = (target[u] - current_sum[u]) % 2
		y[e] = y_val
		determined[e] = True
		current_sum[v] = (current_sum[v] + y_val) % 2
		if e in undetermined_sets[v]:
			undetermined_sets[v].remove(e)
		if len(undetermined_sets[v]) == 1:
			q.append(v)

	responses: list[tuple[int, int]] = []
	for i in range(number_of_ribs):
		u, v = edges[i]
		responses.append((u, v) if y[i] == 0 else (v, u))

	return responses

if __name__ == '__main__':
	# количество вершин, количество ребер
	number_of_vertices, number_of_ribs = [int(value) for value in input().split()]

	ribs = []
	for i in range(number_of_ribs):
		data = input().split()
		ribs.append((int(data[0]), int(data[1])))

	response = task_6(number_of_vertices, number_of_ribs, ribs)

	if len(response) == 0:
		print(-1)
		exit()

	for res in response:
		print(*res)
