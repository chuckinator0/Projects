'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
			  5
			/   \
		   2     13

Output: The root of a Greater Tree like this:
			 18
			/   \
		  20     13
'''
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# iterative approach.
def convertBST(root):
	# x is the running sum of all nodes to the right of the 
	# current node.
	x = 0
	stack = []
	node = root

	# Traverse down the right side as much as possible, building up
	# a stack. Eventually we reach a leaf and set node to None
	while node or stack:
		while node:
			stack.append(node)
			node = node.right
		# At this point, we went past a leaf to None, so we step back
		# to the leaf.
		node = stack.pop()
		# add the running sum to the current node value
		temp_value = node.val
		node.val += x
		# update the running sum to include the current value
		x += temp_value
		# Take a step to the left and then continue going
		# right as much as possible
		node = node.left

	# Now we have updated the values of every node in the tree, so we return
	# the root.
	return root



# in order to pass the running sum by reference, we have to turn it
# into a mutable object (here, a list of size 1)
## From leetcode, it seems these values are accumulating
## every time the function is called, which it shouldn't be?

# editing more. learned about using "nonlocal" instead of "global"
# It is still not working with leetcode, but that might be because 
# of how they set up the Solution() class

# editing back to use the singleton
def convertBST2(root, x = [0]):
	if not root:
		return None
	convertBST2(root.right,x)
	temp_value = root.val
	root.val += x[0]
	x[0] += temp_value
	convertBST2(root.left,x)
	return root

# leetcode solution passing a reference using classes
class Solution:
    def __init__(self):
        self.sums = 0
        
    def convertBST(self,root):
        if not root:
            return None
        self.convertBST(root.right)
        temp_value = root.val
        root.val += self.sums
        self.sums += temp_value
        self.convertBST(root.left)
        return root

# The following was accepted by leetcode.
# We have to define the function outside of the solution class
# and then call the function within the class. We use singleton
# to pass the variable by reference
def convertBST3(root, x = [0]):
	if not root:
		return None
	convertBST3(root.right,x)
	temp_value = root.val
	root.val += x[0]
	x[0] += temp_value
	convertBST3(root.left,x)
	return root

class Solution:
    def convertBST(self, root):
        return convertBST3(root, x = [0])









