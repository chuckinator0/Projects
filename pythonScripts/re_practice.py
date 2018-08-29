import re

string = "hello Long 86 bal .. dfsjldf ,: \n hello"

#string = re.findall(r"[\w']+", string)

string = re.sub(r"\W",'',string)
"""
The "re" module is the regular expression module. The r character signals we are not ignoring special characters.
In this line, we are substituting everything that is not a word character ([\W]) with an empty string.
Note that [\w] is the set of word characters and [\W] is the set of non-word characters. See https://docs.python.org/3/library/re.html
for more info.
"""

print(string)