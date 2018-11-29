"""
Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].
"""


def composeRanges(array):
	# we don't want to modify the input array
	nums = array.copy()

	ranges = []
	while nums:
		start = end = nums.pop(0)
		# end keeps increasing by 1 until there is a jump
		while nums and nums[0] - end == 1:
			end = nums.pop(0)
		# append start -> end to the ranges. If end and start are the same (i.e a jump happened that gave a range of size 1), then we append empty string (i.e. do nothing)
		ranges.append( str(start) + ( '', '->' + str(end) )[start != end] )
	return ranges

print(composeRanges([-1, 0, 1, 2, 6, 7, 9]))

"""
This piece of line 22 is curious:

str(start) + ( '', '->' + str(end) )[start != end]

So there's a tuple ('', '->' + str(end)). We append the string at index [start != end]. If start == end, then start != end evaluates to 0 (False), which means
we append the string at index 0 of the tuple. If start != end, then start != end evaluates to 1, and we append the string at index 1. Kind of a clever way
to avoid using more if statements to decide what to append.

"""