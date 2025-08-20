
def task_3(peoples: int, energies: list[int], links: list[list[int]]) -> int:
	graph: list[list[int]] = [[] for _ in range(peoples)]

	for (people_1, people_2) in links:
		graph[people_1 - 1].append(people_2)
		graph[people_2 - 1].append(people_1)

	peoples_energy = {people: energies[people] for people in range(peoples)}
	sorted_peoples_energy = {key: value for key, value in sorted(peoples_energy.items(), key = lambda pair: pair[1])}

	visited_peoples = {people: False for people in range(peoples)}
	min_energy = 0

	for people, energy in sorted_peoples_energy.items():
		if visited_peoples[people]:
			continue

		min_energy += energy

		stack = [people]
		while stack:
			people = stack.pop()

			if visited_peoples[people]:
				continue

			visited_peoples[people] = True

			for friend in graph[people]:
				stack.append(friend - 1)

	return min_energy

if __name__ == '__main__':
	peoples = int(input())
	energies = [int(value) for value in input().split()]

	connections = int(input())
	links = [[int(value) for value in input().split(' ')] for _ in range(connections)]

	min_energy = task_3(peoples, energies, links)

	print(min_energy)
