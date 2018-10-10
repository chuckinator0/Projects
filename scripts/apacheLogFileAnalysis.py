'''
Every row is a request on a web server. Some are pages, some are images, some are JavaScript files. That's not the important part now.
Currently we are going to focus on the first field of every line which is the IP address of the requester. We go with a simple exercise.

As you might know, every device uses the IP address 127.0.0.1 to refer to itself. So visitors arriving from that IP address are based on the same machine.

The task is to write a scrip that will count how many requests came from 127.0.0.1 and how many from elsewhere?
'''

# assume log file is in the same directory as this script
file = './apacheLogFileAnalysis.log'

with open(file,'r') as log:
	# keep a count of the localhost requests (requests originating from the local machine)
	count_localhost_requests = 0
	# keep a count of other requests
	count_outside_requests = 0
	for line in log:
		# split the line into a list so that we can extract the IP address
		line = line.split(' ')
		# if we have a request from localhost, increase its counter
		if line[0] == '127.0.0.1':
			count_localhost_requests += 1
		# there is a line with a newline character so I want to exclude that
		elif line[0] == '\n':
			continue
		# if we have a request that's not localhost, increase that counter
		else:
			count_outside_requests += 1
	print('There are {} localhost requests and {} outside requests' .format(count_localhost_requests,count_outside_requests))