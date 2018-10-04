'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

def majorityElement(array):
	# if the array has length 1, then the majority element is the only element
	if len(array) == 1:
		return array[0]
	# Dictionary has the form {number: count of number in the array}
	count_dict = {}
	n = len(array)
	for element in array:
		if element in count_dict:
			# add one to its count and check if it's the majority element
			count_dict[element] += 1
			if count_dict[element] > n // 2:
				return element
		# if the element isn't in the dictionary yet, initialize it with a 
		# count of 1
		else:
			count_dict[element] = 1
	# If we loop through the entire array and haven't found a majority element,
	# return None. Although this problem says there will always be one.
	return None

array = [3,2,3,1,2,3,3]
print(majorityElement(array))