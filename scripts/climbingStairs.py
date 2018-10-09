'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# I actually have done this before with my students!
# The number of ways to get to the nth step is the number of ways to get to n-1 (just need a 1-hop from there) PLUS
# the number of ways to get to n-2 (just a 2-hop from there).
# So the total number of ways to get to the nth step is the nth fibonacci number.
# Here, we count fibonacci numbers starting from 0 (i.e. there is 1 way to go up 0 steps)

# Let's do a dynamic approach, keeping a memo for previously computed fibonacci numbers

def climbStairs(n, memo = {}):
	if n < 0:
		raise Exception('input can\'t be negative')
	elif n < 2:
		return 1
	elif n in memo:
		return memo[n]
	else:
		nth_fib = climbStairs(n-1,memo) + climbStairs(n-2,memo)
		memo[n] = nth_fib
		return nth_fib

n = 10
print ('There are {} ways to go up {} steps' .format( climbStairs(n), n ) )