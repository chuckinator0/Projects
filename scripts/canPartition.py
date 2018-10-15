'''
knapsack problem

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

def canPartition(array):
	if not array:
		return False

	array.sort()
	lower_sum = array[-1]
	higher_sum = sum(array[:-1])
	i = 0
	while i < len(array)//2:
		if lower_sum == higher_sum:
			return True
		elif higher_sum < lower_sum:
			return False
		else:
			lower_sum += array[i]
			higher_sum -= array[i]
			i += 1
	return False

arr1 = []
arr2 = [1,5,11,5]
arr3 = [1,2,3,4]
arr4 = [1,2,3,5]
arr5 = [1,1,1]
arr6 = [3,3,3,4,5]

print(canPartition(arr6))
