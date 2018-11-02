'''
Building the power set of a list. Exploring this code from this source: https://codereview.stackexchange.com/questions/178225/computing-the-powerset-of-a-list
'''

# Use generators for more space efficient computation. Generators yield instead of return. Generators turn functions into iterators.
# Note that we are yielding (as opposed to returning) individual elements of the power set, not the entire power set at once.
# Also note that we are yielding lists rather than sets.
def powerSet(A):
	if A == []:
		# Our base case is the power set of the empty set, which is the singleton [ [] ].
		# Remember we are only yeilding elements of the power set, not the power set itself.
		# We can think og the powerSet() generator itself as the power set.
		yield []
	else:
		new = A[0] # our 'new' element that we are adding to the previous power set
		# powerSet(A[1:]) is the power set of all elements we've added before.
		# For each set in the power set we've built so far, yield the sets we already have, as well as each set with
		# the new element added
		for tail in powerSet(A[1:]):
			yield tail
			yield [new] + tail

A = ['a','b','c','d']
# Instead of printing the result of a function, we instead iterate over the generator, printing each result.
for subset in powerSet(A):
	print(subset)