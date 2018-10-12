'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

# Some commentary. Note that isPalindromicSubstring(input_string, i, j)
# gives the same result as ( isPalindromicSubstring(input_string, i+1, j-1) AND input_string[i]==inputstring[j] )
# because we just go one character in on each side, maintaining the palindrome property. That means we can 
# use a base cases:
#	isPalindromicSubstring(input_string, i, i) = True because each single character is a palindrome, and
#	isPalindromicSubstring(input_string, i, i+1) = (input_string[i]==input_string[i+1]) because two repeated characters make a palindrome
# We can build a set of palindromic substrings, starting with single characters, then two repeated characters, and then
# use the property isPalindromicSubstring(input_string, i, j) == ( isPalindromicSubstring(input_string, i+1, j-1) AND input_string[i]==inputstring[j] )
# to build larger palindromes
def isPalindromicSubstring(input_string, i, j, memo = set()):
	'''
	Returns memo set of palindromic substrings {(S_i,S_j)} if substring S_i...S_j is a palindrome
	'''
	# Our memo is a set of tuples of the form (i,j) that records
	# whether isPalindromicSubstring(input_string,i,j) is true.
	# We check the memo first for the smaller palindrome from i+1 to j-1.
	if (i+1,j-1) in memo and input_string[i] == input_string[j]:
		memo.add((i,j))
		return memo

	# Our base cases.
	# First, check whether the two positions are actually the same position.
	# If so, add them to the memo and return true, since a single character is a palindrome
	if i == j:
		memo.add((i,j))
		return memo
	# Let's check whether we are looking at two adjacent characters
	elif j == i+1:
		# if they are the same letter, then we have aa, bb, cc, etc, which is a palindrome
		if input_string[i] == input_string[j]:
			memo.add((i,j))
			return memo
		# if they are not the same letter, then it's not a palindrome
		else:
			return memo
	# recursively check whether cutting off the end characters results in a palindrome. If 
	# cutting off the end characters makes a palindrome, and then the end characters are the same,
	# then we have a palindrome including the end characters as well. e.g. Look at aabaa.
	# Cutting off the endpoints gives aba, which is a palindrome, and then the endpoints are the same character
	# a == a, so aabaa is also a palindrome.
	if (i+1,j-1) in isPalindromicSubstring(input_string,i+1,j-1,memo) and input_string[i] == input_string[j]:
		memo.add((i,j))
	
	return memo



def longestPalindrome(input_string):
	if input_string == '':
		return ''
	longest = 0
	longest_palindrome = ''
	memo = set()
	for i in range(len(input_string)):
		for j in range(i,len(input_string)):
			if (i,j) in memo:
				palindrome = input_string[i:j+1]
				length = len(palindrome)
				if length > longest:
					longest = length
					longest_palindrome = palindrome
			else:
				memo.union( isPalindromicSubstring(input_string,i,j,memo) )
				if (i,j) in memo:
					palindrome = input_string[i:j+1]
					length = len(palindrome)
					if length > longest:
						longest = length
						longest_palindrome = palindrome
	return longest_palindrome


string = 'abbacdefg'
print(isPalindromicSubstring(string,0,3))

string2 = 'blahabablahfooooooof'
print(longestPalindrome(string2))



