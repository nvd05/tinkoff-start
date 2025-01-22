'''
input:  1-6,8-9,11
output: 1 2 3 4 5 6 8 9 11
'''

# from pprint import pprint


user    = input()
display = []

for range_buffer in user.split(','):
	range_interval = range_buffer.split('-')

	if len(range_interval) == 1:
		display.append(int(range_buffer))
		continue

	range_min = int( range_interval[0] )
	range_max = int( range_interval[1] )

	for number_symbol in range(range_min, range_max + 1):
		display.append(number_symbol)

display.sort()
symbols = [str(number) for number in display]

# pprint(display)
print(' '.join(symbols))
