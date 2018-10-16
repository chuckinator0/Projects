'''
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

Commentary: this is knapsack 0/1 problem in disguise.
'''

def helper(array,target):
	# Initialize a memo. Here, memo[sum] is True if it's possible to
	# achieve a sum of 'sum' with a subarray of the input array.
	# We eventually want to find whether it's possible to achieve a sum of
	# target, so the length of the memo goes from 0 to target (i.e. len = target + 1)
	memo = [False]*(target + 1)
	# If we choose no elements of the array, we will have achieved a sum
	# of zero, so memo[0] is True. This is the base case.
	memo[0] = True

	for value in array:
		temp_memo = [False]*(target + 1)
		for j in range(0,target+1 - value):
			if memo[j]:
				temp_memo[j + value] = True
		for i in range(target+1):
			memo[i] = memo[i] or temp_memo[i]

	return memo[target]


def canPartition(array):
	# If it's possible to partition into two subarrays of equal sum, then the
	# total sum must be even. By contrapositive, if the total sum is odd,
	# then it must be impossible to partition into two subarrays of equal sum.
	if sum(array) % 2 == 1:
		return False

	return helper(array,sum(array)//2)


arr1 = []
arr2 = [1,5,11,5]
arr3 = [1,2,3,4]
arr4 = [1,2,3,5]
arr5 = [1,1,1]
arr6 = [3,3,3,4,5]
arr7 = [1,2,5]

print(canPartition(arr7))
