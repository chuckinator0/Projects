'''
Invert a binary tree.

Example:

Input:

	 4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

	 4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def invertTree(root):
	if root:
		# if there are both children, switch 'em
		if root.left and root.right:
			root.left, root.right = root.right, root.left
		# if there are no children, we've reached a leaf and
		# we can just return the current node (nothing to switch)
		elif (not root.left) and (not root.right):
			return root
		# At this point, if root.left exists, it means root.right is None.
		# Switch 'em!
		elif root.left:
			root.left, root.right = None, root.left
		# at this point, if root.right exits, it means root.left is None.
		# Switch em
		elif root.right:
			root.left, root.right = root.right, None
		# invert at the left child
		invertTree(root.left)
		# invert at the right child
		invertTree(root.right)
	# now that everthing has been switched, return the root node that encapsulates the info of the whole tree
	return root
