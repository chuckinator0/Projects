"""
parsing exercise on 'cron for parsing exercise.dms'
"""

import re
import datetime

#searching for CROND jobs
regex = "CROND\[[0-9]*\]: \(root\) CMD (.*)"

# {command:[last time command was called, total number of times called, sequence of timedeltas]}
crond_dict = {}

def find_datetime(line):
	return datetime.datetime.strptime(line[0:15], "%b %d %H:%M:%S" )


with open('./cron_parse.dms', 'r') as file:
	for line in file:
		# search for crond job
		s = re.search(regex, line)
		# set the time the command occured
		time = find_datetime(line)
		if s:
			# group by command name
			# for some reason I can't set s.group(1) as a variable
			if s.group(1) not in crond_dict:
			#  Record first call of command
				crond_dict[s.group(1)] = [time,1]
			else:
				# append time delta since last call
				crond_dict[s.group(1)].append(time - crond_dict[s.group(1)][0])
				# update the time since last call
				crond_dict[s.group(1)][0] = time
				# increment number of calls
				crond_dict[s.group(1)][1] += 1

command_id = 1
for command in crond_dict:
	# we could print many time deltas just to be sure that it's consistent,
	# but for cleanliness we'll just print the last delta
	print("command number", command_id,"was called", crond_dict[command][1],"times","with frequency", crond_dict[command][-1], "\n")
	command_id += 1
