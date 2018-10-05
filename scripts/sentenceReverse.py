'''
Sentence Reverse

You are given an array of characters arr that consists of sequences of characters separated by space characters. Each space-delimited sequence of characters defines a word.

Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

Explain your solution and analyze its time and space complexities.

Example:

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
				'm', 'a', 'k', 'e', 's', '  ',
				'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
		  'm', 'a', 'k', 'e', 's', '  ',
		  'p', 'e', 'r', 'f', 'e', 'c', 't' ]
'''

# first attempt
def reverse_words(arr):
	'''
	The main idea here is to read each character starting from the end and 
	going backwards, maintaining a queue for each word so the word will read forwards.
	append the word queue onto an output list and return that list.
	'''
	# The output will be this list of characters with the words reversed
	reversed_sentence = []
	# we will build each word with a queue
	word = []
	# start at the end of the array
	i = len(arr) - 1
	while i >= 0:
		character = arr[i]
		# while the character is not a space, insert it into the word queue
		while character != ' ':
			word.insert(0,character)
			# decriment index
			i -= 1
			# at this point, we might have finished processing the whole array, so
			# we add on the word (no space since we are at the end) and
			# return the reversed sentence
			if i < 0:
				reversed_sentence.extend(word)
				return reversed_sentence
			# iterate the character
			character = arr[i]
		# if we get here, it means we hit a space. append a space to the word
		word.append(' ')
		# add on the word to the sentence
		reversed_sentence.extend(word)
		# reset to the next word
		word = []
		# decriment index
		i -=1
		reversed_sentence.extend(word)

arr = ['a', 'b', ' ',
	  'c', ' ',
	  'd', 'e', 'f']
print(reverse_words(arr))