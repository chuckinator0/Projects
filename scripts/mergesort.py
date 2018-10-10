'''
Mergesort!
'''

def merge(left, right):
	"""
	This function merges two sorted subarrays into one sorted array.
	"""
	result = []
	left_index = 0
	right_index = 0

	# We check each subarray from left to right, appending the lower value
	# to a result array. The left_index is updated when a value from the left
	# subarray is appended, and vice versa with the right_index.
	while left_index <  len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			result.append(left[left_index])
			left_index += 1
		else:
			result.append(right[right_index])
			right_index += 1
	# One of the arrays might be longer than the other. In which case, we just append the rest of whichever
	# array is longer
	try:
		result.extend(left[left_index:])
	except IndexError:
		pass
	try:
		result.extend(right[right_index:])
	except IndexError:
		pass
			

	return result

left = [1,2,3,4]
right = [3,4,5,6]
print(merge(left,right)) # should give [1,2,3,3,4,4,5,6]




def mergeSort(array):
	"""
	Divide, conquer, and combine to sort an array.
	We break the array into parts [leftpoint, ..., midpoint,..., endpoint] -> [leftpoint,...,midpoint] and [midpoint+1,...,endpoint]
	We recursively sort the subarrays and merge the sorted subarrays together. The base case is a singleton array.
	"""
	length = len(array)
	# The base case. A singleton array is very easy to sort because it's already sorted.
	if length == 1:
		return array
	# this is the midpoint of the array (rounded down)
	midpoint = length // 2

	# create sorted subarrays. The left subarray goes from the beginning to the midpoint.
	left = mergeSort( array[ : midpoint] )
	# The right subarray goes from the midpoint to the end.
	right = mergeSort( array[ midpoint : ] )

	# merge the sorted subarrays and return the sorted list!
	return merge(left,right)

array = [1,4,3,6,2,5,7,8,2,4,8,4,9,9,5,1,2]

print(mergeSort(array)) # should give [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9]


