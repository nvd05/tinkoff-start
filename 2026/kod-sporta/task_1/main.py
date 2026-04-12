
def solve():
	n = int(input().strip())

	evens = n // 2
	odds = (n + 1) // 2

	print(evens * odds)

if __name__ == '__main__':
	solve()
