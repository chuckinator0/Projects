'''
Just playing with permutations
'''
import itertools
s = "abcdef"

print(list(itertools.permutations(s)),"\n")

'''
Now without cheating with itertools
'''

def perm(s):
	# input: string of unique characters
	# output: list of permutations of input string
	def helper(s,i):
		# returns a list of all permutations of s[:i+1] (s up to index i)
		# if we are going up to index 0, we just return a list whose only element is itself a singleton list
		if i == 0:
			return [ [ s[0] ] ]
		# previous is a list of permutations of s up to index i-1
		previous = helper(s,i-1)
		current = []
		# n is the length of a permutation in the previous output
		n = len(previous[0])
		# for each previous permutation, we will insert the new character s[i] into every possible position to get a new
		# permutation on s[:i+1]
		for prev_perm in previous:
			for j in range(n+1):
				temp = prev_perm.copy()
				temp.insert(j,s[i])
				current.append(temp)
		return current
	# for all permutations of s, return all permutations of s up to index len(s)-1 (i.e. s from 0 to len(s)-1, all characters of s)
	return helper(s,len(s)-1)


print(perm(s))





