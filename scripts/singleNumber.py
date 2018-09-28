'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

def singleNumber(nums):
	# initialize a set of unique items
	unique_set = set()
	for item in nums:
		# if an item isn't already in the unique set, add it to the unique set
		if item not in unique_set:
			unique_set.add(item)
		# if the item is already in unique set, it's no longer unique, so remove it
		else:
			unique_set.remove(item)
	# At this point, the only element to survive the loop will be the one element that is
	# not repeated
	return unique_set.pop()

# keep in mind that this function doesn't work if the input has greater than 2 repetitions since they
# would be erroniously added to the unique set.

# Another solution that doesn't use extra memory would be using XOR (bit manipulation)

def singleNumberXOR(nums):
	a = 0
	for i in nums:
	    a ^= i
	return a

nums = [4,1,2,1,2]
print(singleNumber(nums))
print(singleNumberXOR(nums))




