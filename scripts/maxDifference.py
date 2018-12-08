"""
Find the maximum difference between an element of a list and all the elements that came before it.
For example, take arr = [1,2,5,9].
For 1, we don't compare to anything since it's the first element.
For 2, we look at [1] and the difference is [1]
For 5, we look at [1,2] and the differences are [4,3]
for 9, we look at [1,2,5] and the differences are [8,7,4]
The greatest difference among all of the differences is 8.
If the input list has all non-positive differences, return -1.
"""

def maxDiff(arr):
	max_difference = -1

	for i in range(len(arr)):
		differences = [ arr[i]-k for k in arr[:i+1] ]
		local_max_difference = max(differences)
		if local_max_difference > 0 and  local_max_difference > max_difference:
			max_difference = local_max_difference
	return max_difference

print(maxDiff([5,4,3,2]))

