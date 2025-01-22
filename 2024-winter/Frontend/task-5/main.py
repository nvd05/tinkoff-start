'''
1)

00:00:00
5
"VK" 00:10:21 A FORBIDEN
"T" 00:00:23 A DENIED
"T" 00:20:23 A ACCESSED
"VK" 00:30:23 A ACCESSED
"YA" 00:40:23 B ACCESSED

1 "T" 1 40
1 "YA" 1 40
3 "VK" 1 50

2)

01:00:00
3
"Team1" 01:10:00 A FORBIDEN
"Team1" 01:20:00 A ACCESSED
"Team2" 01:40:00 B ACCESSED

1 "Team1" 1 40
1 "Team2" 1 40

3)

23:00:00
2
"Team1" 23:59:59 A PONG
"Team1" 00:00:00 A ACCESSED

1 "Team1" 1 60
'''

# from pprint import pprint
from re     import match


# { team_name: { server_name: { state: bool, total_mins: int } } }
teams = {}

run_time_event = input()
req_count      = int(input())

def get_diff_minute (begin_time: str, end_time: str) -> int:
	begin_time_values = match('(\d\d):(\d\d):(\d\d)', begin_time)
	end_time_values   = match('(\d\d):(\d\d):(\d\d)', end_time)

	begin_hour        = int( begin_time_values.group(1) )
	begin_minute      = int( begin_time_values.group(2) )
	begin_second      = int( begin_time_values.group(3) )

	end_hour        = int( end_time_values.group(1) )
	end_minute      = int( end_time_values.group(2) )
	end_second      = int( end_time_values.group(3) )

	if end_time < begin_time:
		offset_hour = 24 - begin_hour
		begin_hour  = 0

		end_hour += offset_hour

	diff_hour   = end_hour   - begin_hour
	diff_minute = end_minute - begin_minute
	diff_second = end_second - begin_second

	# ===== ===== ===== ===== =====

	response = 0

	response += (diff_hour * 60)
	response += diff_minute

	return response

for _ in range(req_count):
	buffer = input()
	values = match('"([^"]*)" (\d\d:\d\d:\d\d) (\w) (ACCESSED|DENIED|FORBIDEN|PONG)', buffer)

	team_name   = values.group(1)
	time_event  = values.group(2)
	server_name = values.group(3)
	state       = values.group(4)

	if state == 'PONG':
		continue

	# ===== ===== ===== ===== =====

	if not team_name in teams:
		teams[team_name] = {}

	servers = teams[team_name]

	# ===== ===== ===== ===== =====

	if not server_name in servers:
		servers[server_name] = {
			'state'      : False,
			'total_mins' : 0
		}

	server = servers[server_name]

	# ===== ===== ===== ===== =====

	if state in ( 'DENIED', 'FORBIDEN' ):
		server['total_mins'] += 20
		continue

	# ACCESSED

	server['state']       = True
	server['total_mins'] += get_diff_minute(run_time_event, time_event)

# pprint(teams)

# ===== ===== ===== ===== =====
# посчитать количество взломанных серверов у команд
# ===== ===== ===== ===== =====

teams_servers = []

for team_name, team_data in teams.items():

	team_servers = {
		'team_name'  : team_name,
		'count'      : 0,
		'total_mins' : 0
	}

	for server_name, server_data in team_data.items():

		if server_data['state'] == False:
			continue

		team_servers['count']      += 1
		team_servers['total_mins'] += server_data['total_mins']

	teams_servers.append(team_servers)

# pprint(teams_servers)

# ===== ===== ===== ===== =====
# sort
# ===== ===== ===== ===== =====

teams_sorted = sorted(teams_servers, key = lambda team: (team['count'], team['total_mins']))

# pprint(teams_sorted)

# ===== ===== ===== ===== =====
# print
# ===== ===== ===== ===== =====

back_count = 0
back_mins  = 0

offset = 1
memory_offset = 0

for team in teams_sorted:

	curr_team_count = team['count']
	curr_team_mins  = team['total_mins']

	if curr_team_count != back_count or curr_team_mins != back_mins:
		offset += memory_offset

	print(f"{ offset } \"{ team['team_name'] }\" { curr_team_count } { curr_team_mins }")

	memory_offset += 1
	back_count = curr_team_count
	back_mins  = curr_team_mins
