
# from pprint import pprint

# ===== ===== ===== ===== =====

line_1 = input().split(' ', 2)

employees     = int(line_1[0])
employee_time = int(line_1[1])

# ===== ===== ===== ===== =====

floors = [int(floor) for floor in input().split(' ', employees)]

# ===== ===== ===== ===== =====

employee_identifier = int(input())

# ===== ===== ===== ===== =====

# print('employees: %s' % (employees, ))

# print('employee_identifier: %s' % (employee_identifier, ))
# print('employee_time: %s' % (employee_time, ))

# pprint(floors)

# ===== ===== ===== ===== =====

floor_min = floors[0]
floor_cur = floors[employee_identifier - 1]
floor_max = floors[len(floors) - 1]

# print('floor_min: %s' % (floor_min, ))
# print('floor_cur: %s' % (floor_cur, ))
# print('floor_max: %s' % (floor_max, ))

diff_max = floor_max - floor_cur
diff_min = floor_cur - floor_min

# если до этажа дойдем быстрее, чем закончится время.
if diff_min <= employee_time or diff_max <= employee_time:
	print(floor_max - floor_min)
else:
	if diff_max <= diff_min:
		# print('max')
		print(diff_max * 2 + diff_min)
	else:
		# print('min')
		print(diff_min * 2 + diff_max)
