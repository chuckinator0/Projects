import random


def quickselect(l, k ):
	"""
	quickly selects the kth smallest element from the list l (starting from 1).
	"""
	if len(l) == 1:
		return l[0]

	# Choose a random pivot
	pivot = random.choice(l)

	# low is a list of numbers less than or equal to the pivot.
	# included case when the list contains None elements
	low = [num for num in l if num <= pivot]
	# high is a list of numbers greater than the pivot.
	high = [num for num in l if num > pivot]

	# if the low list's length is greater than k, then the kth smallest element is the kth smallest element of low as well.
	if k <= len(low):
		# recursively find the kth smallest element of the low list
		return quickselect(low,k)
	# if the kth smallest element is in the high list, then we can get rid of the low list and find the k-len(low)th smallest
	# element of the high list.
	else:
		k = k - len(low)
		return quickselect(high,k)