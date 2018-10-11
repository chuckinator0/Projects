'''
Implement radix sort!
Great for those times where you have a really big array, but the VALUES in the array
are small.
'''
#I'm going to use the deque library to make queues
from collections import deque


def radixSort(array, maximum_places):
	# we assume the input has at most maximum_places number of place-value places
	# create a bucket (queue) for each digit 0-9
	buckets = [deque() for i in range(10)]

	# turn all the elements of the array into strings and padd them with 0's
	# so they are all length of maximum_places
	for i in range(len(array)):
		array[i] = f"{array[i]:0{maximum_places}}"

	for place in reversed(range(maximum_places)):
		# for this place, we go through the array, putting
		# elements into the buckets by digit. Everything with a 0
		# at this place goes in the 0 bucket, etc.
		for element in array:
			digit = int(element[place])
			buckets[digit].append(element)
		# Now we pop from all the digit queues to populate the array, now
		# sorted by this particular place value.
		i = 0
		for digit in range(10):
			while buckets[digit]:
				array[i] = buckets[digit].popleft()
				i += 1
	# At this point, we have sorted by each digit from ones to 10s to 100s etc.
	# We can turn each element back into an integer
	for i in range(len(array)):
		array[i] = int(array[i])

	return array





array1 = []
array2 = [4]
array3 = [5,4]
array4 = [100,982,3,25,8,592,98,9,2,1,5]

print( radixSort(array4, 3) )

#### A fun aside using .format() and f-strings for string formatting in order to turn
# a positive number into a string and pad it with 0s.
x = 23
maximum_digits = 5

print( "{0:{1}}".format(x,maximum_digits) )
print( f"{x:0{maximum_digits}}" )
