"""
DeepSeek
"""


def task_4(count: int, games: list[tuple[int, int, int]]) -> int:
	l_list = [game[0] for game in games] # i => i - 1
	r_list = [game[1] for game in games] # i => i + 1
	a_list = [game[2] for game in games] # емкость

	left_dp = [0] * (count + 1)
	right_dp = [0] * (count + 1)

	# left
	for i in range(1, count):
		left_dp[i] = min(l_list[i], a_list[i - 1] + left_dp[i - 1])

	# right
	for i in range(count - 2, -1, -1):
		right_dp[i] = min(r_list[i], a_list[i + 1] + right_dp[i + 1])

	max_water = 0
	for i in range(0, count):
		total_water = a_list[i] + left_dp[i] + right_dp[i]
		if total_water > max_water:
			max_water = total_water

	return max_water

if __name__ == '__main__':
	count = int(input())
	games: list[tuple[int, int, int]] = []

	for i in range(count):
		data = input().split()
		games.append((int(data[0]), int(data[1]), int(data[2])))

	response = task_4(count, games)
	print(response)
