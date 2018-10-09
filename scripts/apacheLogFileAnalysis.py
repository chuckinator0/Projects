'''
Every row is a request on a web server. Some are pages, some are images, some are JavaScript files. That's not the important part now.
Currently we are going to focus on the first field of every line which is the IP address of the requester. We go with a simple exercise.

As you might know, every device uses the IP address 127.0.0.1 to refer to itself. So visitors arriving from that IP address are based on the same machine.

The task is to write a scrip that will count how many requests came from 127.0.0.1 and how many from elsewhere?
'''

# assume log file is in the same directory as this script
file = './apacheLogFileAnalysis.log'

with open(file,'r') as log:
	count_localhost_requests = 0
	count_outside_requests = 0
	for line in log:
		line = line.split(' ')
		if line[0] == '127.0.0.1':
			count_localhost_requests += 1
		elif line[0] == '\n':
			continue
		else:
			count_outside_requests += 1
	print('There are {} localhost requests and {} outside requests' .format(count_localhost_requests,count_outside_requests))