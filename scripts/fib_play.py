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