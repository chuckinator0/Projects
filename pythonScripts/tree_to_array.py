'''
Given the root node of a binary tree, produce the array form of the binary tree,
ignoring null entries (I want to ignore null entries so I can implement
quickselect to find the kth smallest element in the tree better)

Oof. For one, the indentation is messed up because I made the mistake of
copying a pasting some code from leetcode. More importantly, I decided that
this problem I made for myself isn't well posed. I don't have a standard input
of tree nodes from which to build my program. Perhaps if the standard input was
a list or dictionary of TreeNode() objects, this would make sense.
Then we could take the nodes from the given input and us something resembling
this program to create a list of values with the desired structure:
[root, child1, child2, child11, child12, child21, child22, etc.]

I'm abandoning this, but I will keep it as a record of what I learned about
making well posed problems for myself.
'''

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def createArray(root):
  '''
  Input: root node of a binary tree
  Output: array form of binary tree without the None placeholders
  We need to exclude the Nones so we can use quickselect.
  We can do breadth first search to traverse the tree
  '''
  queue = []
  queue.insert(0,root)
  output = []

  while queue:
    node = queue.pop()
    output.append(node.val)
    if node.left is not None:
    	# this doesn't work because we should already have nodes of the tree
    	# predefined. We shouldn't be creating a node here.
    	left_node = TreeNode(node.left)
		queue.insert(0,left_node)
    if node.right is not None:
      right_node = TreeNode(node.right)
      queue.insert(0,right_node)

  return output


# Make a binary tree
'''
    3
   / \
  2   7
   \
    4
'''
node3 = TreeNode(3)
node3.left = 2
node3.right = 7

node2 = TreeNode(2)
node2.left = None
node2.right = 4

node4 = TreeNode(4)
node4.left = None
node4.right = None

node7 = TreeNode(7)
node7.left = None
node7.right = None


print(createArray(node3))