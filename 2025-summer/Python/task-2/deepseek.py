
n = int(input())
branches = []
for _ in range(n):
	a, b = map(int, input().split())
	branches.append((a, b))
q = int(input())
for _ in range(q):
	t, d = map(int, input().split())
	t -= 1  # переход к 0-индексации
	a, b = branches[t]
	if d < a:
		print(a)
	else:
		delta = d - a
		k = (delta + b - 1) // b
		print(a + k * b)
