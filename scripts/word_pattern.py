"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
"""

def check_letter(letter, word, letter_to_word_dict, word_to_letter_dict):
	if letter_to_word_dict[letter] == word and word_to_letter_dict[word] == letter:
		return True
	else:
		return False

letter_to_word_dict = {}
word_to_letter_dict = {}

def wordPattern(pattern, string):
	wordlist = string.split()
	if len(pattern) != len(wordlist):
		return False
	for i in range(len(wordlist)):
		if pattern[i] not in letter_to_word_dict:
			letter_to_word_dict[pattern[i]] = wordlist[i]
		if wordlist[i] not in word_to_letter_dict:
			word_to_letter_dict[wordlist[i]] = pattern[i]
		if not check_letter(pattern[i], wordlist[i], letter_to_word_dict, word_to_letter_dict):
			return False
	return True

string = ""
pattern = ""

print(wordPattern(pattern,string))