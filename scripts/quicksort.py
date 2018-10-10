'''
Implementing quicksort!
Pivot, partition, recurse!

Pretty cool interactive resource: http://me.dt.in.th/page/Quicksort/
'''

# We are going to choose pivots randomly to avoid the situation where data is 
# cherry picked to slow down quicksort at the midpoint.
import random

# Some commentary. Quicksort is a lot like mergesort in the sense that we
# break into left and right subarrays and sort them recursively. But quicksort doesn't
# do the "merge" step. Instead, quicksort picks a pivot, pushes everything
# less than the pivot the left and everything else to the right. In this way, they pivot
# is guaranteed to be in the correct *position* of the eventually sorted list. Only THEN
# do we recurse on the left and right subarrays. This is still O(n*log(n)), but is 
# often faster than mergesort in practice. Quicksort's partitioning phase also differs from
# mergesort because it doesn't create extra arrays. It changes the array in-place.

def quicksort( array, low, high ):
	# low is the starting index of the left subarray, and high is the highest
	# index the subarray reaches (plus one, because Python counts from zero).
	# This is important when we recurse.

	# Base case. A singleton array is already sorted! We can assume our array has two or more elements after this.
	if len(array[low:high]) <= 1:
		return array

	# pick an index at random to be the pivot element
	pivot_index = random.choice( range(low,high) )
	pivot = array[pivot_index]

	# Now, we partition the array into a left subarray, the singleton pivot, and a right subarray.
	# [...left...][pivot][...right...]
	# The left partition is all elements less than the pivot. The right partition is all elements
	# greater than or equal to the pivot.

	# First, we swap the pivot with the leftmost element and then start scanning from left to right.
	# When we find an element greater than or equal to the pivot, we will record it and continue scanning until
	# we find an element less than the pivot, then swap those elements. Once we get to the end of the
	# list (so our index is one to the right of the end), we swap the pivot with the element that comes before the current recorded value.

	# swap pivot to the leftmost position
	array[low], array[pivot_index] = array[pivot_index], array[low]

	# imagine all the elements right of the pivot are cards face down. We open a card and check its value. If the value is less than the pivot,
	# we swap it with the current card. We only update this index after a swap. We are remembering the leftmost element and index that is greater than
	# the pivot so we can swap it when we find a value less than the pivot.
	remembered_index =  low + 1

	for index in range(low + 1,high):
		if array[index] < pivot:
			# if we open a card less than the pivot, we swap and update the current index
			array[remembered_index], array[index] = array[index], array[remembered_index]
			remembered_index += 1
		# if we find an element greater than equal to pivot, we don't swap and we don't update
		# the remembered index.

	# At this point, array[remembered_index] is the leftmost element in the array that is greater
	# or equal to the pivot. We now swap the pivot with the spot just to the left of array[remembered_index].
	pivot_index = remembered_index - 1
	array[low], array[pivot_index] = array[pivot_index], array[low]


	# Now the pivot is in the correct sorted position in the list, since everything to the left is less
	# and everything to the right is greater or equal.
	# Now, we recursively call quicksort on the left and right subarrays
	# Notice we are just calling these functions, not taking up extra space by assigning their 
	# return values. The processes happening on these subarrays is mutating array itself.
	quicksort( array, 0, pivot_index )
	quicksort( array, pivot_index + 1,  high)

	# We have now mutated the array to put every element in its correct sorted position
	return array


array1 = []
array2 = [4]
array3 = [5,4]
array4 = [1,4,3,5,77,7]

print(quicksort(array4, 0, len(array4)))










