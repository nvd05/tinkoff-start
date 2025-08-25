
def task_2(games: list[tuple[int, list[int]]])-> list[str]:
	results = []

	for (game_count, game_array) in games:
		game_array.sort()

		valid = True
		for i in range(game_count):
			if game_array[i] > i + 1:
				valid = False
				break

		if not valid:
			results.append("Second")
			continue

		total_moves = 0
		for i in range(game_count):
			total_moves += (i + 1 - game_array[i])

		if total_moves % 2 == 1:
			results.append("First")
		else:
			results.append("Second")

	return results

if __name__ == '__main__':
	games_count = int(input())
	games_array: list[tuple[int, list[int]]] = []

	for _ in range(games_count):
		game_count = int(input())
		game_array = [int(char) for char in input().split()]

		games_array.append((game_count, game_array))

	responses = task_2(games_array)

	for response in responses:
		print(response)
