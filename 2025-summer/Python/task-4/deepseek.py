
n = int(input())
A = list(map(int, input().split()))
n = len(A)  # для случая, если ввод не соответствует, но по условию соответствует

i_max_for_k = [-1] * n
last_occurrence = {x: -1 for x in range(1, 11)}  # Хранит последнее вхождение каждого числа от 1 до 10

for k in range(n):
	current_value = A[k]
	# Обновляем последнее вхождение текущего значения
	last_occurrence[current_value] = k

	# Проверяем все возможные possible_j_value от 1 до 10
	for possible_j_value in range(1, 11):
		j = last_occurrence.get(possible_j_value, -1)
		if j == -1 or j >= k:
			continue

		required_i = 2 * possible_j_value - current_value
		if required_i < 1 or required_i > 10:
			continue

		i = last_occurrence.get(required_i, -1)
		if i == -1 or i >= j:
			continue

		if i > i_max_for_k[k]:
			i_max_for_k[k] = i

# Вычисляем префиксный максимум
prefix_max = [-1] * n
current_max = -1
for r in range(n):
	current_max = max(current_max, i_max_for_k[r])
	prefix_max[r] = current_max

# Считаем результат
result = 0
for r in range(n):
	if prefix_max[r] >= 0:
		result += (prefix_max[r] + 1)

print(result)
