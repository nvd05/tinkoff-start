from collections import deque


def min_cycle_length(n, adj):
	min_cycle = float('inf')
	
	for start_node in range(n):
		dist = [-1] * n
		parent = [-1] * n
		queue = deque([start_node])
		dist[start_node] = 0
		
		while queue:
			u = queue.popleft()
			
			for v in adj[u]:
				if dist[v] == -1:
					dist[v] = dist[u] + 1
					parent[v] = u
					queue.append(v)
				elif parent[u] != v:
					# Найден цикл, проверяем его длину
					min_cycle = min(min_cycle, dist[u] + dist[v] + 1)
					
	return min_cycle if min_cycle != float('inf') else 0

def task_4(n, m, edges):
	# Создаем список смежности с индексацией от 0
	adj = [[] for _ in range(n)]
	
	for a, b in edges:
		# Преобразуем номера вершин из 1-based в 0-based
		adj[a-1].append(b-1)
		adj[b-1].append(a-1)
	
	result = min_cycle_length(n, adj)
	return -1 if result == 0 else result

def main():
	data = input().strip().split()

	n, m = map(int, data)
	edges = []
	
	for _ in range(m):
		a, b = input().strip().split()
		a, b = int(a), int(b)
		edges.append((a, b))

	result = task_4(n, m, edges)
	print(result)

if __name__ == '__main__':
	main()
