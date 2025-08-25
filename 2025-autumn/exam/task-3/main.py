"""
DeepSeek
"""

from collections import defaultdict


mod = 10 ** 9 + 7

def task_3(numbers: list[int]) -> int:
	count = defaultdict(int)
	for number in numbers:
		count[number] += 1

	result = 1
	for key in count:
		result = (result * (count[key] + 1)) % mod

	result = (result - 1) % mod
	return result

if __name__ == '__main__':
	count = int(input())

	numbers = [int(value) for value in input().split()]
	response = task_3(numbers)
	print(response)
