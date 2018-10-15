'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

def maxProfit(array):
	# Our overall goal here is to buy low and sell high.
	# initialize profit
	profit = 0
	# initialize the indices for a potential buy and a potential sell.
	i = 0
	j = i+1
	while j < len(array):
		# The index i is where we are thinking about buying. The
		# index j is where we are thinking about selling.
		potential_buy = array[i]
		potential_sell = array[j]
		# if the value of the potential sell is actually less than the
		# potential buy, it means we've found a value lower than our
		# potential buy. We want to buy low, so we will update our
		# potential buy index to this new index so that when we return to 
		# the beginning of the loop, our potential buy is this new, lower value.
		# we also want to update the potential sell index so that we are looking at the next stock in the list.
		if potential_sell < potential_buy:
			i = j
			j += 1
			continue
		# if we get here, it means we have found a stock that is less or equal in value than 
		# our current potential buy, so there is a chance for some profit
		else:
			# our potential profit is the selling price - buying price. If that profit is greater than the current
			# profit, we update our profit so that it will reflect the maximum profit
			if potential_sell - potential_buy > profit:
				profit = potential_sell - potential_buy
			# regardless of whether we increased our profit, we want to look at the 
			# next stock to see if we get a bigger profit.
			j += 1
	# if we get here, it means we have looked through the whole list for potential sells.
	# we return the maximum profit that we found in the process.
	return profit

stocks = [5,3,8,1,5,6,7]
stocks1 = []
stocks2 = [2,5,1]
stocks3 = [5,4,3]
stocks4 = [2,2,3,4,1]
stocks5 = [2,2,3,4,1,3]
stocks6 = [2,2,3,4,1,5]
print(maxProfit(stocks6))





