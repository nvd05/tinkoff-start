
def task_1(numbers: list[int]) -> list[str]:
	operations = 0
	stages = []

	numbers.reverse()

	for number in numbers:
		operations += 1

		# новый подход
		if number == 1:
			stages.append(str(operations))
			operations = 0

	if operations != 0:
		stages.append(str(operations))

	stages.reverse()

	return stages

if __name__ == '__main__':
	count = int(input())
	numbers = [int(value) for value in input().split()]

	stages = task_1(numbers)

	print(len(stages))
	print(' '.join(stages))
