'''
At CodeSignal the users can get to the top of the leaderboard by earning XP (experience points) in different modes.
The leaderboard is sorted by players XP in descending order, and in case of a tie - by their ids in ascending order.

Your task is to implement an algorithm that will return the state of the weekly leaderboard given a list of users.

Example

For

users = [["warrior", "1", "1050"],
		 ["Ninja!",  "21", "995"],
		 ["recruit", "3", "995"]]
the output should be
sortCodesignalUsers(users) = ["warrior", "recruit", "Ninja!"].
'''

class CodeSignalUser():
	
	def __init__(self,name, ID, points):
		self.name = name
		self.ID = int(ID)
		self.points = int(points)
	
	# if we don't do this, the output of sortCodesignalUsers would be a list
	# of CodeSignalUser objects rather than strings. __repr__ gives us a rule
	# for how to represent our objects.
	def __repr__(self):
		return self.name
	
	# We need to define how to tell whether one CodeSignalUser object is less than
	# another using the __lt__ method.
	def __lt__(self,other):
		# If points are equal, we say self is less than other if its ID is greater.
		# In other words, smallest ID wins ties.
		if self.points == other.points:
			return self.ID > other.ID
		else:
			return self.points < other.points

def sortCodesignalUsers(users):
	res = [CodeSignalUser(*user) for user in users]
	res.sort(reverse=True)
	return list(map(str, res))

users = [["warrior", "1", "1050"],
		 ["Ninja!",  "21", "995"],
		 ["recruit", "3", "995"]]
print(sortCodesignalUsers(users))