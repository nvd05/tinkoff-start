
n = int(input())
A = []
B = []
for _ in range(n):
	ai, bi = map(int, input().split())
	A.append(ai)
	B.append(bi)
q = int(input())
for _ in range(q):
	ti, di = map(int, input().split())
	line = ti - 1
	a = A[line]
	b = B[line]
	diff = di - a
	k = max(0, (diff + b - 1) // b)
	next_train = a + k * b
	print(next_train)
