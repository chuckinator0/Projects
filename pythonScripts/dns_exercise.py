'''
This file answers questions about a DNS packet dump. The packet file is dns.cap. In order to turn
that file into a parsable log, I used the terminal command `tcpdump -r dns.cap > dns_log`, which
converts the contents of dns.cap into a dns log and writes that information to a file called dns_log.

Exercises
1. What is the IP address of www.netbsd.org?
2. For what domain was there a mail exchange lookup?
3. Name a mail exchange server for google.com!
4. For what domain was there a name server lookup?

'''
import re

file_path = './dns_log'


# print the IP address of www.netbsd.org
with open(file_path, 'r') as file:
	# keep track of which line we are on
	line_number = 1
	# when there is a request, we will remember which line it happened on
	request_line = 0
	for line in file:
		line_split = line.split(' ')
		netbsd = re.search('netbsd',line)
		ip4_request = re.search(' A\? ', line)
		response = re.search(' A ', line)
		# remember the line that makes a request for www.netbsd.org
		if netbsd and ip4_request:
			request_line = line_number
		# the response is on the next line after the request,
		# so we print the IP address
		if response and line_number == request_line + 1:
			print('The ip for netbsd is {}\n' .format(line_split[-2]))
		line_number += 1

# Find a line where there was a mail exchange and print it out.
# The output shows us that the domain is google.com with mail ex servers
# smtp[integers 1 through 6].google.com
with open(file_path, 'r') as file:
	for line in file:
		line_split = line.split(' ')
		mail_exchange = re.search(' MX ', line)
		if mail_exchange:
			print(line)

# print out a site for which there was an ANY (name server) lookup
with open(file_path, 'r') as file:
	for line in file:
		line_split = line.split(' ')
		name_server = re.search('\sANY\?\s',line)
		if name_server:
			print(line_split[-2])



