
def task_2(directions: str) -> bool:
	count = {
		'E': 0, # x +1
		'W': 0, # x -1
		'N': 0, # y +1
		'S': 0, # y -1
	}

	for direction in directions:
		count[direction] += 1

	if (count['E'] > 0 and count['W'] == 0) or (count['E'] == 0 and count['W'] > 0):
		return False
	elif (count['N'] > 0 and count['S'] == 0) or (count['N'] == 0 and count['S'] > 0):
		return False

	return True


if __name__ == '__main__':
	directions = input().strip()
	status = task_2(directions)
	print('Yes' if status else 'No')
