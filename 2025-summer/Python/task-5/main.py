
# deepseek

n, a, b = map(int, input().split())
s = list(input())

cnt_open = s.count('(')
delta = cnt_open - n
cost = 0

if delta > 0:
	# Replace excess '(' with ')'
	positions = [i for i, c in enumerate(s) if c == '(']
	to_replace = positions[-delta:]
	for i in to_replace:
		s[i] = ')'
	cost += delta * b
elif delta < 0:
	delta_abs = -delta
	# Replace excess ')' with '('
	positions = [i for i, c in enumerate(s) if c == ')']
	to_replace = positions[-delta_abs:]
	for i in to_replace:
		s[i] = '('
	cost += delta_abs * b

# Now calculate the number of swaps needed
opens = []
for i in range(len(s)-1, -1, -1):
	if s[i] == '(':
		opens.append(i)

balance = 0
swap_count = 0
j = 0

for i in range(len(s)):
	if s[i] == '(':
		balance += 1
	else:
		balance -= 1

	if balance < 0:
		# Find the next available '('
		while j < len(opens) and opens[j] <= i:
			j += 1
		if j < len(opens):
			swap_count += 1
			balance += 2  # After swap, current becomes '('
			j += 1

cost += swap_count * a
print(cost)
