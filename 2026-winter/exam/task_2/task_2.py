
def task_2(input_string: str) -> int:
	s = input_string.strip()
	n = len(s)
	
	# Подстроки, которые мы ищем
	tbank = 'tbank'
	study = 'study'
	len_t = len(tbank)  # 5
	len_s = len(study)  # 5
	
	# Если длина строки меньше суммы длин подстрок (10),
	# то подстроки должны пересекаться
	if n < len_t + len_s:
		# Перебираем все возможные позиции для обеих подстрок
		best = float('inf')
		
		# Перебираем начало для tbank
		for i in range(n - len_t + 1):
			# Перебираем начало для study
			for j in range(n - len_s + 1):
				# Проверяем, могут ли обе подстроки существовать одновременно
				# Создаем копию строки или считаем изменения
				changes = 0
				valid = True
				
				# Для каждой позиции в строке
				for k in range(n):
					# Какие символы нужны в этой позиции?
					need_t = None
					need_s = None
					
					# Если позиция k входит в tbank
					if i <= k < i + len_t:
						need_t = tbank[k - i]
					
					# Если позиция k входит в study
					if j <= k < j + len_s:
						need_s = study[k - j]
					
					# Если нужны оба символа и они разные - невозможно
					if need_t is not None and need_s is not None and need_t != need_s:
						valid = False
						break
					
					# Определяем, какой символ должен быть в этой позиции
					need = need_t if need_t is not None else need_s
					
					# Если символ нужен (всегда должен быть, так как подстроки покрывают всю строку или часть)
					if need is not None and s[k] != need:
						changes += 1
				
				if valid:
					best = min(best, changes)
		
		return best if best != float('inf') else n
	
	# Для строк длиной >= 10 используем оптимизированный алгоритм
	# Вычислим стоимость превращения каждого отрезка длины 5 в tbank и study
	cost_tbank = [0] * (n - len_t + 1)
	cost_study = [0] * (n - len_s + 1)
	
	for i in range(n - len_t + 1):
		for k in range(len_t):
			if s[i + k] != tbank[k]:
				cost_tbank[i] += 1
	
	for i in range(n - len_s + 1):
		for k in range(len_s):
			if s[i + k] != study[k]:
				cost_study[i] += 1
	
	# Префиксные и суффиксные минимумы для cost_study
	m = n - len_s + 1
	pref_min = [float('inf')] * m
	suff_min = [float('inf')] * m
	
	if m > 0:
		pref_min[0] = cost_study[0]
		for i in range(1, m):
			pref_min[i] = min(pref_min[i - 1], cost_study[i])
		
		suff_min[m - 1] = cost_study[m - 1]
		for i in range(m - 2, -1, -1):
			suff_min[i] = min(suff_min[i + 1], cost_study[i])
	
	ans = float('inf')
	
	# Перебираем позицию для tbank
	for i in range(n - len_t + 1):
		# Случай 1: непересекающиеся подстроки (расстояние >= 5)
		# study слева от tbank
		if i >= len_s:
			ans = min(ans, cost_tbank[i] + pref_min[i - len_s])
		# study справа от tbank
		if i + len_t + len_s - 1 < n:
			j = i + len_t
			if j < m:
				ans = min(ans, cost_tbank[i] + suff_min[j])
		
		# Случай 2: пересекающиеся подстроки
		# Перебираем возможные начала для study в окрестности i
		start_j = max(0, i - len_s + 1)
		end_j = min(m - 1, i + len_t - 1)
		
		for j in range(start_j, end_j + 1):
			# Определяем границы пересечения
			left = max(i, j)
			right = min(i + len_t - 1, j + len_s - 1)
			
			# Проверяем совместимость в области пересечения
			compatible = True
			total_cost = cost_tbank[i] + cost_study[j]
			
			# Учитываем пересечение
			for k in range(left, right + 1):
				idx_t = k - i
				idx_s = k - j
				if tbank[idx_t] != study[idx_s]:
					compatible = False
					break
				# Если символы совпадают, но в исходной строке он неправильный,
				# то мы учли изменение дважды (в cost_tbank и cost_study)
				if s[k] != tbank[idx_t]:
					total_cost -= 1
			
			if compatible:
				ans = min(ans, total_cost)
	
	return ans

if __name__ == '__main__':
	s = input()
	result = task_2(s)
	print(result)
