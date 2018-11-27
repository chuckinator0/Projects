def fib(n):
	'''
	print nth fibonacci number, n > 1
	'''
	if n ==1:
		return 1

	# The n-2 fibonacci number
	two_back = 0
	# The n-1 fibonacci number
	one_back = 1

	for _ in range(n-1):
		# This is the fibonacci relation
		next_fib = two_back + one_back
		# now, increment what is the n-2 and what is the n-1 fibonacci number
		two_back, one_back = one_back, next_fib
	return next_fib


print([fib(i) for i in range(1,6)])


## With generators this time!

def fib2():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b

result = fib2()
for i in range(40):
	print(result.__next__())
	

