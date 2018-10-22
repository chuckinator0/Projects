'''
Consider a special family of Engineers and Doctors. This family has the following rules:

Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
Given the level and position of a person in the ancestor tree above, find the profession of the person.
Note: in this tree first child is considered as left child, second - as right.
'''

'''
dynamic programming solution. This is exponential time, O(2^level), since we are processing each node in the tree.
We can optimize a little by checking whether we have found
(level,pos) in the middle of the while loop and stop.
'''
def findProfession(level, pos):
        # make a memo to track earlier outputs {(level,position) : "Doctor" or "Engineer"}
        # For simplicity, we can have True represent Engineer and False represent Doctor.
        memo = {(1,1): True}
        # Our inductive step:
        # memo[(i,j)] == memo[(i+1,2*j-1)] and memo[(i+1,2*j)] = not memo[(i,j)]
        # In other words, when we go a level down from (i,j), the value on the left
        # (which will now be at position 2*j-1) is equal to the value at (i,j), and 
        # The value to the right (at position 2*j) will be the opposite of the value at
        # (i,j).
        i = 1
        while i < level:
                temp_memo = {}
                for tup in memo:
                        j = tup[1]
                        temp_memo[(i+1,2*j-1)] = memo[(i,j)]
                        temp_memo[(i+1,2*j)] = not memo[(i,j)]
                for new_tup in temp_memo:
                        memo[new_tup] = temp_memo[new_tup]
                i += 1
        if memo[(level,pos)]:
                return "Engineer"
        else:
                return "Doctor"

'''
A better solution would be to keep in mind the number of switches as we go down the tree. If we go left, there is no
switch. If we go right, the profession switches. There are 2^(level-1) professions in the level we are examining. Consider
level =4, pos = 3:
                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D *D* E  D   E E   D
The number of switches for each position: 
0
0 1
0 1, 1 2
0 1, 1 2, 1 2, 2 3
0 1, 1 2, 1 2, 2 3, 1 2, 2 3, 2 3, 3 4 

Each position in one level spawns two new positions on the next level. The number of switches on the left is the same, and the number of
switches on the right is one greater.
'''
def switch_array(level):
	'''
	Input a level of the binary tree (counting from level 1 as the root).
	Output an array of the number of switches for each position on this level.
	'''
	switch_arr = [0]
	for i in range(level-1):
		temp = [k + 1 for k in switch_arr]
		switch_arr.extend(temp)
	return switch_arr

#print(switch_array(3))



def findProfession2(level,pos):
	switch_arr = switch_array(level)
	if switch_arr[pos-1] % 2 == 0:
		return "Engineer"
	else:
		return "Doctor"


#print(findProfession2(25,1000))

'''
This is faster than it was before, only timing out of one test rather than two. AHA. Tricksy, this is. By cheating,
I have learned that we can use binary representation to help us out.
'''

def findProfession3(level,pos):
    bits  = bin(pos-1).count('1')
    if bits%2 == 0: 
        return "Engineer"
    else:
        return "Doctor"

'''
I don't understant this very well yet.
'''

'''
Here's a different approach. If you number the nodes:
                1
           /         \
          2           3
        /   \        /  \
       4     5      6      7
      / \   /  \    / \    / \
     8   9 10   11  12 13 14  15
then the node at (level,pos) will have label k = 2^level + position-1. The parent node will have label
floor(k/2). We need to take the label of the node, and recurse up the tree to see how many switches (right paths)
there are.
'''


