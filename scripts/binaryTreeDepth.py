'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

	3
   / \
  9  20
	/  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Try a recursive approach
def maxDepth(root, max_depth = 0, current_path = []):
	# if the tree is empty, then its depth is 0
	if not root:
		return 0
	# append the current node to te current path
	current_path.append(root)
	# update the value of max_depth if the current path is larger than it
	if len(current_path) >  max_depth:
		max_depth = len(current_path)
	# go to the left child, remembering the current path and current max_depth value
	if root.left:
		left_max = maxDepth(root.left,max_depth,current_path)
		# if our path took us further, we update our max_depth
		if left_max > max_depth:
			max_depth = left_max
	# once we have gone as far left as possible, we go right, again
	# remembering the current path and current value of max_depth
	if root.right:
		right_max = maxDepth(root.right, max_depth, current_path)
		# again, if this path took us further than we've gone before,
		# update the max_depth
		if right_max > max_depth:
			max_depth = right_max
	# At this point, we have gone left and we have gone right, so we delete this
	# node from the current path.
	del current_path[-1]
	# We have updated the max_depth for every path from the root to every leaf
	# below the current node. Now we return the result, which is the maximum depth
	# of all these paths.
	return max_depth

# Let's test by making a binary tree and finding its depth!
'''
	4
   / \
  2   5
	   \
		6
'''
node_dict = {}
for i in range(1,7):
	node_dict[i] = TreeNode(i)

node_dict[4].left = node_dict[2]
node_dict[4].right = node_dict[5]
node_dict[2].left = None
node_dict[2].right = None
node_dict[5].left = None
node_dict[5].right = node_dict[6]

node_dict[6].left = None
node_dict[6].right = None

print(maxDepth(node_dict[4]))

##### Other solutions by other people, and me trying to explain them in my own words

## Here's another recursive solution that is mcuh cleaner
def maxDepth2(root):
	# The max depth is one more than the max depth
	# of its deepest subtree.
	if root:
		return 1+ max( maxDepth2(root.left), maxDepth2(root.right) )
	# if root is None, it means the previous node passed a None child.
	# By returning 0, we make sure that we don't add to the depth.
	else:
		return 0

## Here's an iterative solution that seems to crawl down the tree one level at a time. I like it!
def maxDepth3(root):
	md = 0
	# if we are passed an empty tree, return depth 0
	if not root:
		return md
	# populate a list that contains all elements of the tree at the current depth.
	# Right now, we are at the root so the list contains just the root
	current = [root]
	# while the current level of the tree is not empty...
	while current:
		# create a new list of all nodes on the next level down
		new = list()
		# append all children of nodes in the current level to get all the nodes
		# in the next level down
		for node in current:
			if node.left:
				new.append(node.left)
			if node.right:
				new.append(node.right)
		# we have now gone down a level, so we update what we call the current level
		current = new
		# since we have gone down a level, we add 1 to the depth
		md += 1
	# at this point, we have gone down, level by level, until we get to a level
	# that contains no nodes. We have incremented the depth each time it was possible to go
	# down a level, so the current value of md is the maximum depth.
	return md
















