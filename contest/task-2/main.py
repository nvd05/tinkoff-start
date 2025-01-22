
peoples = int(input())

actions = 0
parts   = 1

while parts < peoples:
	actions += 1
	parts   *= 2

print(actions)
