def fib(n):
	'''
	print nth fibonacci number
	'''
	if n in [0,1]:
		return n

	# The n-2 fibonacci number
	two_back = 1
	# The n-1 fibonacci number
	one_back = 1

	for _ in range(n):
		# This is the fibonacci relation
		next_fib = two_back + one_back
		# now, increment what is the n-2 and what is the n-1 fibonacci number
		two_back = one_back
		one_back = next_fib
	return next_fib



def fib_dynamic(n):
	'''
	fibonacci with dynamic programming
	'''
	pass



def fib_explicit(n):
	'''
	compute fib(n) explicitly with a formula
	'''
	pass


print(fib(5))