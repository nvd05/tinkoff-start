
def task_3(t: int, s_arr: list) -> str:
	'''
	Решение задачи. Принимает входную строку, возвращает строку с ответами.
	'''

	out = []

	for s in s_arr:
		n = len(s)

		# Если строка целиком из единиц
		if '0' not in s:
			out.append(str(n * n))
			continue

		# Максимальная длина последовательных единиц внутри строки
		max_inner = 0
		cur = 0
		for ch in s:
			if ch == '1':
				cur += 1
				if cur > max_inner:
					max_inner = cur
			else:
				cur = 0

		# Длина префикса из единиц
		pref = 0
		for ch in s:
			if ch == '1':
				pref += 1
			else:
				break

		# Длина суффикса из единиц
		suff = 0
		for ch in reversed(s):
			if ch == '1':
				suff += 1
			else:
				break

		# Максимальный циклический отрезок из единиц
		M = max(max_inner, pref + suff)
		# Максимальная площадь: (M+1)*(M+1)//4
		ans = (M + 1) * (M + 1) // 4
		out.append(str(ans))

	return '\n'.join(out).strip()

if __name__ == '__main__':
	t = int(input())
	s = [input() for _ in range(t)]

	print(task_3(t, s))
