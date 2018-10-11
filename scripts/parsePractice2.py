'''
Short Parse Challenge of the day:
write all agent names as piglatin (first letter at the end + 'ay')
In: 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
Out: 'Agent liceAay told Agent arolCay that Agent veEay knew Agent obBay was a double agent.'
'''

import re

sentence = "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent."

reg = re.compile(r'Agent (\w)(.?(?=[aeiou]))(\w*)')
new_sentence = reg.sub(r'Agent \3\2\1ay', sentence)
print(new_sentence)