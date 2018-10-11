'''
Implement insertion sort!
'''

def insertionSort(array):
	# We iterate through the list
	for i in range(len(array)):
		# at this position in the list, we introduce a new index that will go backwards to the beginning
		j = i
		while j >= 0:
			# if the value at the current index is less than at an index that came before, remove the
			# value from the list and insert it before the element it is less than.
			if array[i] < array[j]:
				sorted_element = array.pop(i)
				array.insert(j, sorted_element)
			# keep moving backwards to the beginning of the list
			j -= 1
	return array

'''
Some commentary. In the best case of an already sorted array, insertion sort is O(n) since we would only compare
each element to the element to its left (one comparison per element, so n comparisons).

In the worst case, we would have an array in reverse order, so we would have to compare each element to every element on its left,
every single time. This would be O(n^2), since we would be comparing each element to nearly an entire list each time.

On average, insertion sort is also O(n^2) since we aren't breaking the sort into smaller subproblems each time like quicksort
or mergesort. However, insertion sort is faster than quicksort on small arrays, and it also very fast for arrays that are *nearly* sorted
(since )
'''

array1 = []
array2 = [5,4]
array3 = [2]
array4 = [1,2,3,2,5,6]

print( insertionSort(array4) )