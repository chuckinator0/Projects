'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

def carryOne(digits,index):
	'''
	carries the 1 while necessary
	'''
	if digits[index] == 9:
		# set the current digit to 0
		digits[index] = 0
		# keep carrying until you get to a digit that isn't 9.
		# If we have an index error, it means we have 9999.. and need a new digit
		try:
			carryOne(digits,index-1)
		except IndexError:
			digits.insert(0,1)
	else:
		digits[index] += 1
	return digits
	

def plusOne(digits):
	if digits[-1] < 9:
		digits[-1] += 1
		return digits
	else:
		return carryOne(digits,-1)

digits = [9,9,9]
print(plusOne(digits))
