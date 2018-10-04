'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

# This probably doesn't count since I'm using extra memory with the set
def findDisappearedNumbers(array):
	# make a set {1,2,3,...,n}
	output = set(range(1,len(array)+1))
	# remove each element of the array from the set
	for element in array:
		if element in output:
			output.remove(element)
	# turn the set into a list
	return list(output)

array = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(array))

# Another solution that seems faster in practice. Perhaps appending to a list is faster than
# removing from a set
def findDisappearedNumbers2(array):
	# take the input and turn it into a set
	input_set = set(array)
	# initialize list of numbers missing from the input
	missing = []
	for number in range( 1, len(array) +1 ):
		if number not in input_set:
			missing.append(number)
	return missing

print(findDisappearedNumbers2(array))









