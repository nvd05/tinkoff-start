'''
1)

5
10 2 3 5
5 4
0
4
15 3

25

2)

6
2 2
2 3
15 4
1 5
2 6
0

22

'''

# from pprint import pprint


count_processes = int(input())
processes = []

for _ in range(count_processes):
	buffer  = input()
	options = buffer.split(' ')
	numbers = [int(value) for value in options]

	processes.append({
		'time'          : numbers[0],
		'sub_processes' : numbers[1:]
	})

# pprint(processes)

# ===== ===== ===== ===== =====
# calc
# ===== ===== ===== ===== =====

def get_total_time_process (process_data: dict[str]) -> int:
	time_response = process_data['time']
	sub_processes = process_data['sub_processes']

	sub_processes_times = [get_total_time_process( processes[index - 1] ) for index in sub_processes]
	sub_processes_max   = max(sub_processes_times) if len(sub_processes_times) > 0 else 0

	return time_response + sub_processes_max

calc_total_time_processes = [get_total_time_process(data) for data in processes]

# pprint(calc_total_time_processes)
print(max(calc_total_time_processes))
