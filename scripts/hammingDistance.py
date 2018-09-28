'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2**31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

# This implementation converts to a 32 bit binary string and checks the differences
def hammingDistance(x,y):
	"""
	input: two integers x and y
	output: hamming distance between x and y (integer)
	"""
	# convert x and y to 32 bit binary strings, front filled with 0's
	x_bin = format(x,'032b')
	y_bin = format(y,'032b')

	# count different bits
	count = 0

	for i in range(32):
		if x_bin[i] != y_bin[i]:
			count += 1

	return count

x = 42
y = 7220

print(hammingDistance(x,y))

## Here's another one using bitwise operations
def hammingDistance2(x,y):
	# By doing the XOR operation, we create an integer whose binary representation
	# is 1's wherever x and y's binary representations differ, and 0's where they
	# are the same
	difference = x ^ y
	# We will count the places where x and y's binaries differ
	count = 0
	# We iterate through the bits of difference, increasing the count when the 1's
	# place is 1, and then shifting all the bits to the right one space. Eventually
	# we will have shifted all the 1's to the right so that difference becomes 0.
	# In this way, we have counted all the 1's in difference, which is the number of
	# bits where x and y differ.
	while difference:
		count += difference & 1
		difference >>= 1
	return count



