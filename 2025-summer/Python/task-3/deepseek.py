
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
used = set()
count = 0

for num in a:
	x = num
	while True:
		if x not in used:
			used.add(x)
			count += 1
			break
		new_x = x // 2
		if new_x == x:  # предотвращаем бесконечный цикл при x=0
			break
		x = new_x

print(count)
