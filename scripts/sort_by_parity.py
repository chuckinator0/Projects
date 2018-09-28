'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

def sortArrayByParity(array):
	'''
	input: an array
	output: the array with even elements appearing before odd elements
	'''
	output = []
	for element in array:
		# if element is even, insert it into the beginning of the output array
		if element % 2 == 0:
			output.insert(0,element)
		# if element is odd, append it to the end
		else:
			output.append(element)

	return output

array = [3,1,2,4]
print(sortArrayByParity(array))