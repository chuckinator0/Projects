'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you
from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were
broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

def rob(houses):
	'''
	This function outputs the maximum amount of money we can get from robbing a list
	of houses whose values are the money. To do this, we will find the max amount of money
	to rob sublists houses[0:1], houses[0:2], ..., houses[0:k+1],..., houses[0:len(houses)]

	Let f(k) be the maximum money for robbing houses[0:k+1]. In other words,
	f(k) := rob(houses[0:k]). Notice that we have this relationship:
	f(k) == max( houses[k] + f(k-2), f(k-1) )
	This relationship holds because the maximum money for robbing
	houses 0 through k is either the maximum money for robbing houses
	0 through k-2 plus robbing house k (remember, the houses can't be adjacent),
	or, if house k isn't that much money and house k-1 is, we might get the maximum money from robbing
	houses 0 through k-1 (which puts house k off limits due to the no-adjacency rule).

	Notice that to compute f(k), we only need the values f(k-2) and f(k-1), much like fibonacci.
	So our memo will consist of two variables that keep track of these values and update as k goes from 
	0 to len(houses)-1.
	'''
	# Let's handle the case where the house list is empty
	if not houses:
		return 0
	# Let's handle the cases where the houses list is only one house
	if len(houses) == 1:
		return houses[0]
	# Let's handle the cases where the houses list is only two houses
	if len(houses) == 2:
		return max(houses[0],houses[1])


	# initialize f(k-2) to f(0), where our sublist of houses is just the value of the first house.
	fk_minus2 = houses[0]


	# initialize f(k-1) to f(1), which is the max money for houses[0:3], the first two houses.
	# We just take the max of these two house values.
	fk_minus1 = max(houses[0], houses[1])



	# now we march through the list:houses from position 2 onward, updating f(k-2), f(k-1)
	# along the way
	for house in houses[2:]:
		# The max value we can get robbing houses up to and including this current house is 
		# either this house plus the max value up to 2 houses ago, or the max value up to the last house
		fk = max( house + fk_minus2, fk_minus1)
		# increment k
		fk_minus2, fk_minus1 = fk_minus1, fk

	# At this point, k has reached the end of the list, and so fk represents the maximum money from robbing
	# the entire list of houses, which is the return value of our rob function.
	return fk

houses1 = [1,2,4,2,8] # expect rob(houses1) == 13
houses2 = [] # expect rob(houses2) is None

print(rob(houses1))






