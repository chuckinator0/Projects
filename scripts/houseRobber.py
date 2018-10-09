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

# Brute force: find all the combinations of houses where no two houses are adjacent, and take the combination
# that gives the maximum amount of money.

def rob(house_list, maximum = [0]):
	number_houses = len(house_list)
	for index in number_houses:
		house_value = house_list[index]
		this_max = house_value + rob(house_list[ : index-2 : index+2 : ])
		if this_max > maximum[0]:
			maximum[0] = this_max

