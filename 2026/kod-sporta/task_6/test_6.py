import heapq
import sys

# Увеличиваем лимит рекурсии для глубоких графов
sys.setrecursionlimit(200000)

def task_6(n: int, m: int, a: list[int], adj_in: list[list[int]]) -> list[int]:
	adj = [[] for _ in range(n + 1)]
	for adj_one in adj_in:
		u = adj_one[0]
		v = adj_one[1]
		w = adj_one[2]
		adj[u].append((v, w))
		adj[v].append((u, w))

	# 1. Дейкстра от 1 и от N
	def dijkstra(start_node):
		dists = [float('inf')] * (n + 1)
		dists[start_node] = 0
		pq = [(0, start_node)]
		while pq:
			d, u = heapq.heappop(pq)
			if d > dists[u]:
				continue
			for v, w in adj[u]:
				if dists[u] + w < dists[v]:
					dists[v] = dists[u] + w
					heapq.heappush(pq, (dists[v], v))
		return dists

	d1 = dijkstra(1)
	dn = dijkstra(n)
	min_dist = d1[n]

	# 2. Построение DAG кратчайших путей
	dag_adj = [[] for _ in range(n + 1)]
	for u in range(1, n + 1):
		for v, w in adj[u]:
			if d1[u] + w + dn[v] == min_dist:
				dag_adj[u].append(v)

	# Порядок топологической сортировки по расстоянию d1
	nodes_sorted = sorted(range(1, n + 1), key=lambda x: d1[x])

	# 3. Бинарный поиск по медиане
	sorted_a = sorted(list(set(a)))

	def check(mid_val):
		# b[i] = 1 если оценка >= mid_val, иначе -1
		weights = [1 if val >= mid_val else -1 for val in a]
		dp = [-float('inf')] * (n + 1)
		dp[1] = weights[0] # a[0] соответствует городу 1

		for u in nodes_sorted:
			if dp[u] == -float('inf') or d1[u] > min_dist:
				continue
			for v in dag_adj[u]:
				new_w = dp[u] + weights[v-1]
				if new_w > dp[v]:
					dp[v] = new_w
		return dp[n] > 0

	low = 0
	high = len(sorted_a) - 1
	best_median = sorted_a[0]

	while low <= high:
		mid = (low + high) // 2
		if check(sorted_a[mid]):
			best_median = sorted_a[mid]
			low = mid + 1
		else:
			high = mid - 1

	return [min_dist, best_median]

if __name__ == "__main__":
	n, m = list(map(int, input().split()))
	a = list(map(int, input().split()))
	adj = [list(map(int, input().split())) for _ in range(m)]

	res = task_6(n, m, a, adj)
	print(res[0], res[1])
