
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	if a == 0 or b == 0: return 0
	return abs(a * b) // gcd(a, b)

def task_4(n: int, k: int) -> int:

	# 1. Находим все делители k
	divs = []
	for i in range(1, int(k**0.5) + 1):
		if k % i == 0:
			divs.append(i)
			if i*i != k:
				divs.append(k // i)

	# 2. Считаем, сколько чисел от 1 до n имеют конкретный gcd с k
	# count[g] - сколько x в [1, n] таких, что gcd(x, k) == g
	count = {}
	for d in divs:
		count[d] = 0

	# Эффективный подсчет count[g]
	for i in range(1, n + 1):
		g = gcd(i, k)
		count[g] += 1

	ans = 0
	# 3. Перебираем делители для a и b
	for g_a in divs:
		if count[g_a] == 0: continue
		for g_b in divs:
			if count[g_b] == 0: continue

			# Условие 1: a*b делится на k
			if (g_a * g_b) % k == 0:
				# Условия для c:
				# a*c делится на k => c_gcd делится на k/g_a
				# b*c делится на k => c_gcd делится на k/g_b
				need_c_gcd_to_be_multiple_of = lcm(k // g_a, k // g_b)

				# Считаем сумму count[g_c] для всех g_c, кратных need_c_gcd...
				c_sum = 0
				for g_c in divs:
					if g_c % need_c_gcd_to_be_multiple_of == 0:
						c_sum += count[g_c]

				ans += count[g_a] * count[g_b] * c_sum

	return ans

if __name__ == '__main__':
	n, k = list(map(int, input().split()))
	res = task_4(n, k)
	print(res)
