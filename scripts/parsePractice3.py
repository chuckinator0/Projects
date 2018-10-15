'''
The task is to create a script that can parse such input file and create a hash-of-hashes (dictionary of dictionaries in Python)
where the primary key is the section name, the secondary key is the 'key' and the value is the value in each line.

example INI file:
 
# comment
[alpha]
 
base  = moon
ship= alpha 3
 
[earth]
   # ?
base=London   
ship=  x-wing

The '#' denote comments, the [] represent section names, and the other entries represent key:value pairs
'''

import re

# Here, the brackets can be surrounded by whitespace. The contents in the brackets are captured in a group,
# so the section name can be extracted.
detect_section = re.compile(r'\s*\[(.*)\]\s*')

# Here, we allow the key and value to be surrounded by whitespace. We create a group for the key (left of =)
# and a group for the value (right of the =)
detect_key_val_pair = re.compile(r'\s*(\w.*\w)\s*=\s*(\w.*\w)')

ini_file = './parsePractice3.ini'

with open(ini_file, 'r') as file:
	# our output is a dictionary of dictionaries of the form:
	# {section : dictionary of key value pairs within that section}
	output = {}
	for line in file:
		if re.match(detect_section,line):
			# extract the name of the section
			section = re.match(detect_section,line).group(1)
			# Here we assume sections are unique. If we detect a section,
			# then we initialize its output as a dictionary.
			output[section] = {}
		elif re.match(detect_key_val_pair,line):
			key = re.match(detect_key_val_pair,line).group(1)
			value = re.match(detect_key_val_pair,line).group(2)
			output[section][key] = value
		else:
			# we have not detected a section or a key value pair, so we just continue to the
			# next line.
			continue

print(output)




