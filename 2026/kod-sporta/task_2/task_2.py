
def task_2(data: str):
	n = int(data.strip())

	if n == 1:
		return 0

	total_pairs = (n**2 * (n**2 - 1)) // 2
	attacking_pairs = 4 * (n - 1) * (n - 2)

	return total_pairs - attacking_pairs

if __name__ == "__main__":
	print(task_2(input()))
