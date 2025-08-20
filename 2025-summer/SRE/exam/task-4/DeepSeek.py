
def task_4(d: int, k: int) -> int:
	ans = 0
	n = 1
	for i in range(d):
		mid = 1 << (d - i - 1)
		if k <= mid:
			if n % 2 == 0:
				ans += (1 << (d - i)) - 1
				n += (1 << (d - i))
			else:
				n += 1
		else:
			if n % 2 == 1:
				ans += (1 << (d - i)) - 1
				n += (1 << (d - i))
			else:
				n += 1
			k -= mid

	return ans + d + 1

if __name__ == '__main__':
	d, k = map(int, input().split())

	operations = task_4(d, k)
	print(operations)
