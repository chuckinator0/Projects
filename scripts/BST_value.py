'''
Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Reminder that a binary search tree is one where all values in the left subtree are less than the value of the current node,
# and all values in the right subtree are greater.
def searchBST(root,val):
	'''
	root: TreeNode object, root of the binary search tree
	val: integer, the value we are looking for
	output: return the node whose value is val. If no such node exits, return None
	'''
	stack = []
	node = root
	while node or stack:
		# Traverse down the left side of the tree as much as possible, checking
		# each node against the target value. Eventually, we reach a leaf and set
		# node to None
		while node:
			if node.val == val:
				return node
			stack.append(node)
			node = node.left
		# At this point, we went past a leaf to None, so we step back to the leaf
		node = stack.pop()
		# Take a step to the right and then go back to the while loop to check nodes
		# to the left as much as possible
		node = node.right
	# If we have survived to this point, it means we have traversed the whole tree
	# and not found a node with the target value, so we return None
	return None

## Here's a recursive implementation!

def searchBSTrecursive(root,val):
    '''
    root: TreeNode object, root of the binary search tree
    val: integer, the value we are looking for
    output: return the node whose value is val. If no such node exits, return None
    '''
    # if we have gone to a None node, then we have traversed a subtree that was supposed
    # to contain the target value but failed to find it
    if root is None:
        return None
    # if this node has the target value, return this node
    if root.val == val:
        return root
    # if this node's value is greater than the target value, then
    # the target value is either in the left subtree or it doesn't exist
    if root.val > val:
        return searchBSTrecursive(root.left,val)
    # if this node's value is less than target, then the target value must be
    # in the right subtree or doesn't exist
    else:
        return searchBSTrecursive(root.right,val)






