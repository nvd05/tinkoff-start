
n = int(input())
a = list(map(int, input().split()))

dp = [[-1] * n for _ in range(n)]


def solve(i, j):
	if i >= j:
		return 0
	if dp[i][j] != -1:
		return dp[i][j]

	ans = 0
	for p in range(i, j):
		left_len = p - i
		right_len = j - (p + 1)

		curr = abs(a[p] - a[p + 1])
		curr += solve(i, p - 1)
		curr += solve(p + 2, j)

		if left_len % 2 == 1 and right_len % 2 == 1 and p > i and p + 2 <= j:
			curr += abs(a[p - 1] - a[p + 2])

		ans = max(ans, curr)

	dp[i][j] = ans
	return ans

print(solve(0, n - 1))
