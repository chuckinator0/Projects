'''
Write a Python script that spits out the next scheduled execution in Texas (oof, morbid!)

Sources: 
https://www.pythonforbeginners.com/requests/using-requests-in-python
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html

'''
# BeautifulSoup is a package that helps scrape web sites
from bs4 import BeautifulSoup
# requests package allows us to retrieve information from a website
import requests

r = requests.get('https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html')

# create a soup object from the text of the site using beautifulsoup's html parser
soup = BeautifulSoup(r.text,'html.parser')

# Here, soup.table finds all tables in the html code. The 'children' part finds all the html within the table tag,
# which is all the headers and data entries in the table. Each member of this list is a row in the table.
# If there were multiple tables to deal with, we would just want to check that the caption of the table
# matches the table we want.
table = list(soup.table.children)

# index 3 holds the header information. The get_text() function gets us all the text without the html junk
table_header = table[3].get_text()
# The next person to be executed is at the top of the table, which is at index 5
next_to_be_executed = table[5].get_text()

# Zip together the header with the information from the next person to be executed.
output_list = list(zip(table_header.split('\n'),next_to_be_executed.split('\n')))

# item[0] is the header info and item[1] is the person's info
for item in output_list[1:len(output_list)-1]:
	print(item[0] + ': ' , item[1])
