
def main():
	n = int(input())
	a = list(map(int, input().split()))
	used = set()
	for x in a:
		temp = x
		while temp in used and temp > 0:
			temp = temp // 2
		used.add(temp)
	print(len(used))

if __name__ == "__main__":
	main()
