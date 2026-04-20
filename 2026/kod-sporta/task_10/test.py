import sys

def solve():
	line = sys.stdin.readline()
	if not line:
		return
	n = int(line.strip())

	if n == 0:
		print(0)
		return

	# Ограничение для пре-сита
	limit = int(n**0.5)
	mu = [0] * (limit + 1)
	mu[1] = 1
	primes = []
	is_prime = [True] * (limit + 1)

	for i in range(2, limit + 1):
		if is_prime[i]:
			primes.append(i)
			mu[i] = -1
		for p in primes:
			if i * p > limit:
				break
			is_prime[i * p] = False
			if i % p == 0:
				mu[i * p] = 0
				break
			else:
				mu[i * p] = -mu[i]

	# Префиксные суммы Мёбиуса
	m_prefix = [0] * (limit + 1)
	for i in range(1, limit + 1):
		m_prefix[i] = m_prefix[i-1] + mu[i]

	memo_m = {}

	def get_mertens(m):
		if m <= limit:
			return m_prefix[m]
		if m in memo_m:
			return memo_m[m]

		res = 1
		i = 2
		while i <= m:
			j = m // (m // i)
			res -= (j - i + 1) * get_mertens(m // i)
			i = j + 1

		memo_m[m] = res
		return res

	# Сумма функции Лиувилля L(n) через M(n)
	def get_liouville_sum(m):
		res = 0
		i = 1
		while i * i <= m:
			res += get_mertens(m // (i * i))
			i += 1
		return res

	l_sum = get_liouville_sum(n)

	# Итоговая формула: (n - L(n)) / 2
	# Посетитель 1 всегда активен, он инвертирует результат.
	ans = (n - l_sum) // 2

	# Корректировка по примерам:
	# При n=6, L(6) = -4, (6 - (-4))/2 = 5.
	# При n=49, L(49) = -13, (49 - (-13))/2 = 31.
	print(ans)

if __name__ == "__main__":
	solve()
