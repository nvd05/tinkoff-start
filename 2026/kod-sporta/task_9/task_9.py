import sys

sys.setrecursionlimit(300000)

def task_9(n: int, q: int, peaks: list[int], slats: list[list[int]]) -> list[int]:
	marked_status = peaks
	marked_nodes = [i + 1 for i, v in enumerate(marked_status) if v == 1]

	adj = [[] for _ in range(n + 1)]
	for slat in slats:
		u = slat[0]
		v = slat[1]

		adj[u].append(v)
		adj[v].append(u)

	if not marked_nodes:
		# Если нет отмеченных вершин, это просто расстояние u-v
		# Но по условию обычно хотя бы одна есть.
		pass

	# Стандартный LCA и препроцессинг
	depth = [0] * (n + 1)
	parent = [[0] * 20 for _ in range(n + 1)]
	dist_root = [0] * (n + 1)

	stack = [(1, 0, 0)]
	order = []
	while stack:
		u, p, d = stack.pop()
		parent[u][0] = p
		depth[u] = d
		order.append(u)
		for v in adj[u]:
			if v != p:
				stack.append((v, u, d + 1))

	for j in range(1, 20):
		for i in range(1, n + 1):
			parent[i][j] = parent[parent[i][j-1]][j-1]

	def get_lca(u, v):
		if depth[u] < depth[v]: u, v = v, u
		for j in range(19, -1, -1):
			if depth[u] - (1 << j) >= depth[v]:
				u = parent[u][j]
		if u == v: return u
		for j in range(19, -1, -1):
			if parent[u][j] != parent[v][j]:
				u = parent[u][j]
				v = parent[v][j]
		return parent[u][0]

	def get_dist(u, v):
		return depth[u] + depth[v] - 2 * depth[get_lca(u, v)]

	# 1. Находим общее дерево Штейнера для отмеченных вершин
	# Сортируем отмеченные вершины по времени входа (DFS order)
	# Сумма ребер = (dist(v1, v2) + dist(v2, v3) ... + dist(vk, v1)) / 2
	dfs_idx = [0] * (n + 1)
	for i, node in enumerate(order):
		dfs_idx[node] = i

	marked_nodes.sort(key=lambda x: dfs_idx[x])

	total_steiner_weight = 0
	for i in range(len(marked_nodes)):
		u = marked_nodes[i]
		v = marked_nodes[(i + 1) % len(marked_nodes)]
		total_steiner_weight += get_dist(u, v)
	total_steiner_weight //= 2

	# 2. Обработка запросов
	# Для дерева Штейнера ближайшая точка u_s к u - это либо LCA(u, m) 
	# для какой-то отмеченной вершины m.
	results: list[int] = []
	# Предвычислим LCA всех отмеченных вершин
	common_lca = marked_nodes[0]
	for i in range(1, len(marked_nodes)):
		common_lca = get_lca(common_lca, marked_nodes[i])

	for slat in slats:
		u = slat[0]
		v = slat[1]

		# Функция поиска ближайшей точки в поддереве Штейнера
		def get_closest_in_steiner(x):
			# Ближайшая к x точка в дереве Штейнера - это либо x (если x в дереве),
			# либо LCA(x, m_i), которая глубже всего.
			# Оптимизация: достаточно проверить LCA с m_1, m_k и common_lca
			cand1 = get_lca(x, marked_nodes[0])
			cand2 = get_lca(x, marked_nodes[-1])
			res = cand1 if depth[cand1] > depth[cand2] else cand2
			# Также проверяем, не выше ли это common_lca
			if depth[common_lca] > depth[res]:
				return common_lca
			return res

		u_s = get_closest_in_steiner(u)
		v_s = get_closest_in_steiner(v)

		ans = 2 * total_steiner_weight + get_dist(u, u_s) + get_dist(v, v_s) - get_dist(u_s, v_s)
		results.append(ans)

	return results

if __name__ == '__main__':
	n, q = list(map(int, input().split()))
	peaks = list(map(int, input().split())) # вершины
	slats = [list(map(int, input().split())) for _ in range(n)] # ребра (a, b)

	results = task_9(n, q, peaks, slats)
	print('\n'.join(map(str, results)))
