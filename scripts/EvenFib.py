# By considering the terms in the Fibonacci sequence whose values do not
# exceed m,
# find the sum of the even-valued terms.

Fibonacci = [1,1]
i = 0
while Fibonacci[i] < 4000000:
    Fibonacci.append(Fibonacci[i]+Fibonacci[i+1])
    i += 1

total = 0
for x in Fibonacci:
    if x % 2 == 0:
        total += x

print(total)

'''
We can do better with a memo! Also more general.
'''

def evenFibSum(max_value):
	if max_value < 2:
		return 0
	output_sum = 0
	memo = [1,1] # remember fib n-2, fib n-1
	while memo[1] < max_value:
		if memo[1] % 2 == 0:
			output_sum += memo[1]
		new_fib = memo[0] + memo[1] # get new fib number
		memo[0], memo[1] = memo[1], new_fib # update memo
	return output_sum

print(evenFibSum(4000000))

