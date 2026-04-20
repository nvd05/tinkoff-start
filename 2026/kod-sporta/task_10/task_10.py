from pprint import pprint

def task_10(n: int) -> list[bool]:
	if n == 0:
		return []

	# reverse
	# I [ F, T, T, T, T, T ]
	# 1 [ T, F, F, F, F, F ] (all)
	# 2 [ T, T, F, T, F, T ] (2, 4, 6)
	# 3 [ T, T, T, T, F, F ] (3, 6)
	# 4 [ T, T, T, F, F, F ] (4)
	# 5 [ T, T, T, F, T, F ] (5)
	# 6 [ T, T, T, F, T, T ] (6)

	racks = [True] * n # стойки
	racks[0] = False

	peoples = range(n)

	def toggle_rack(rack_id: int) -> None:
		racks[rack_id] = not racks[rack_id]

	pprint(racks)

	for people in peoples:
		people_id = int(people)
		print('people', people_id + 1)

		if people_id == 0:
			racks = [False] * n
			racks[0] = True

			pprint(racks)
			continue

		for rack in range(0, n + 1, people_id + 1):
			rack_id = int(rack)

			if rack_id == 0:
				continue

			toggle_rack(rack_id - 1)

		pprint(racks)

	return racks

if __name__ == '__main__':
	n = int(input().strip())
	results = task_10(n)

	total = 0
	for item in results:
		if item:
			total += 1

	print(total)
