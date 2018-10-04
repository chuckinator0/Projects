'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

# brute force solution
def moveZeroes(array):
	index = 0
	# we need to keep track of the number of elements processed,
	# or else once we get to the tail of zeros, we would be deleting and
	# appending zeros forever
	elements_processed = 0
	while elements_processed < len(array):
		# if the element is zero, we delete the element and append 0
		# to the end of the array. We have processed an element, but we
		# leave the index where it is to get to the next element.
		if array[index] == 0:
			del array[index]
			array.append(0)
			elements_processed += 1
			continue
		# if the element is not zero, we do nothing to it and just increment
		# the index
		index += 1
		elements_processed += 1


array = [0,1,0,2,0,0,3,4,0,5,6,0,0]
# Calling the function changes array in-place
moveZeroes(array)
print(array)

####### Other solutions by other people

# This is a cool one. We basically find the first nonzero entry and
# swap it with the earliest zero in the list. If there are no zeroes
# early on or at all, the swaps are trivial (swapping an element with itself)
def moveZeroes2(array):
	position_of_earliest_zero = 0
	for i in range(len(array)):
		if array[i] != 0:
			array[i], array[position_of_earliest_zero] = array[position_of_earliest_zero], array[i]
			position_of_earliest_zero += 1

array2 = [1,3,10,0,12,0,0,0,15,0]
moveZeroes2(array2)
print(array2)


