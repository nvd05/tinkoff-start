from collections import Counter


def task_5(n, a):
	cnt = Counter(a)

	res = []
	for i in range(n):
		x = a[i]
		if cnt[x] >= 2:
			ans = n - cnt[x]
		else:
			left = a[(i-1) % n]
			right = a[(i+1) % n]
			if (left >= x and right >= x) or (left <= x and right <= x):
				ans = n - 1
			else:
				ans = n
		res.append(str(ans))

	return ' '.join(res)


if __name__ == '__main__':
	n = int(input())
	a = [int(value) for value in input().split()]

	r = task_5(n, a)
	print(r)
