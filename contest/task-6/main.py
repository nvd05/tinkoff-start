
def find_swap_indices(students: list[int]):
	i = -1
	j = -1

	# Списки для хранения позиций, где ученики стоят неправильно
	even_wrong = [] # Четные на нечетных позициях
	odd_wrong  = [] # Нечетные на четных позициях

	for index, height in enumerate(students, start=1):
		if height % 2 == 0 and index % 2 != 0:
			even_wrong.append(index)
		elif height % 2 != 0 and index % 2 == 0:
			odd_wrong.append(index)

	# Если есть одна ошибка в каждой группе, попробуем поменять их местами
	if len(even_wrong) == 1 and len(odd_wrong) == 1:
		i = even_wrong[0]
		j = odd_wrong[0]

	# Подсмотрел в https://github.com/Ilysikov/TinkoffContest/blob/main/six/six.py
	elif len(even_wrong) + len(odd_wrong) == 0 and len(students) >= 3:
		i = 1
		j = 3

	return i, j

# Чтение входных данных
num_students = int(input())
students     = list(map(int, input().split()))

i, j = find_swap_indices(students)
print(i, j)
