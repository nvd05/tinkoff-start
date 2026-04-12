import sys

def solve():
	# Быстрое чтение всех данных
	input_data = sys.stdin.read().split()
	if not input_data:
		return

	n = int(input_data[0])
	a = list(map(int, input_data[1:]))

	# Создаем список пар (значение, исходный индекс)
	# Исходный индекс нужен для учета "черепах" и стабильности
	indexed_a = []
	for i in range(n):
		indexed_a.append((a[i], i))

	# Стабильная сортировка (Timsort в Python гарантирует стабильность)
	indexed_a.sort()

	max_diff = 0
	for target_idx in range(n):
		original_idx = indexed_a[target_idx][1]
		# Сколько шагов влево нужно сделать элементу
		diff = original_idx - target_idx
		if diff > max_diff:
			max_diff = diff

	print(max_diff)

if __name__ == "__main__":
	solve()
