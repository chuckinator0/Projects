"""
Implementing quickselect to find median
"""
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

def quickselect_median(l):
	"""
	quickly select the median of a list
	"""
	if len(l) % 2 == 1:
		return quickselect(l, len(l)//2 + 1)
	else:
		return (quickselect(l,len(l)/2)+quickselect(l,len(l)/2 +1))/2


l = [1,2,3,4,5,6]
sorted_l = sorted(l)
print(quickselect_median(l))
