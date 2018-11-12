import csv
import sys

ip_dict = {} # {ip address: email}
name = {} # {ip address: name}

file = 'test.csv'

# data has fields ip,name,email
# populate ip_dict and email_dict
with open(file,'r') as inputFile:
	data = csv.DictReader(inputFile, delimiter = ',')
	# skip header row
	next(data)
	# populate ip dictionary with associated alert email address
	for row in data:
		ip_dict[row['ip']] = row['email']
		name[row['ip']] = row['name']

for unresponsiveIP in sys.stdin:
	unresponsiveIP = unresponsiveIP.strip()
	print(
f'Please alert {name[unresponsiveIP]} that {unresponsiveIP} is not responding. Email {ip_dict[unresponsiveIP]}')

