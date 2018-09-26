'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mergeTrees(node1,node2):
	# if nodes 1 and 2 are both None, then the current merged node is None
	# so we won't bother making it
	if (node1 is None) and (node2 is None):
		return None
	# initialize merged node
	merged_node = TreeNode(None)

	# set None values to 0 so we can add them easier
	# also set left and right to None so we can call mergedTrees recurively later
	if node1 is None:
		val1 = 0
		left1 = None
		right1 = None
	else:
		val1 = node1.val
		left1 = node1.left
		right1 = node1.right
	if node2 is None:
		val2 = 0
		left2 = None
		right2 = None
	else:
		val2 = node2.val
		left2 = node2.left
		right2 = node2.right

	# set merged value to the sum
	merged_node.val = val1 + val2

	# initialize left child
	merged_node.left = mergeTrees(left1,left2)

	# initialize right child
	merged_node.right = mergeTrees(right1,right2)

	# return the value of the root of the merged tree
	return merged_node

## Here's a better implementation!

def mergeTrees2(root1,root2):
	# if roots of both trees are None, return None
	if root1 is None and root2 is None:
		return None
	# If root1 is None, but root2 is not None, then we can just return root2 because
	# everything below root1 is None, so we will always just be referencing root2 and its subtree
	if root1 is None:
		return root2
	# Same logic as before
	if root2 is None:
		return root1
	# if we have root1 and root 2, then our merged root value is the sum of their values
	root = TreeNode(root1.val+root2.val)
	# set left node recursively
	root.left = mergeTrees2(root1.left,root2.left)
	# set right node recursively
	root.right = mergeTrees2(root1.right,root2.right)
	# return the root of our merged tree
	return root




