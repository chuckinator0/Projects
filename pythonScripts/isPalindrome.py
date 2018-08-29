import re


def clean_str(s):
	return re.sub(r'\W','',s.lower())

def isPalindrome( s):
	"""
	:type s: str
	:rtype: bool
    """
	s = clean_str(s)
	for index in range(len(s)//2):
		if s[index] != s[-1-index]:
			return False
	return True

print(isPalindrome('abba'))