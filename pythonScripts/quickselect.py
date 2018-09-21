import random


def quickselect(l, k ):
	"""
	quickly selects the kth smallest element from the list l (starting from 1).
	"""
	if len(l) == 1:
		return l[0]

	pivot = random.choice(l)

	low = [num for num in l if num <= pivot]
	high = [num for num in l if num > pivot]

	if k <= len(low):
		return quickselect(low,k)
	else:
		k = k - len(low)
		return quickselect(high,k)