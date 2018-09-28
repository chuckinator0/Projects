'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
'''

## If the binary tree were given in array form, we could remove the None
## values and use quickselect (see quickselect.py) to find the kth
## smallest element. But let's try to use the properties of BST's!


# We can keep in mind that in a Binary Search Tree, each node's value is
# greater than the values of each node in its left subtree and less than
# each 
# left child and less than its right child. I took this code from a leetcode
# solution. My goal is to annotate and document it to understand what each part
# is doing.

class TreeNode:
  def __init__(self,x):
    self.val = x
    self.right = None
    self.left = None

def kthSmallest(root, k):
    stack = []
    # This should work just as well with 'while True'. I'm not sure why we need the 
    # (root or stack) statement.
    while True:
        # Traverse down the left side of the tree as much
        # as you can until you reach a None (going off the tree)
        while root:
            stack.append(root)
            root = root.left
        # Go back up to the leaf
        root = stack.pop()
        # We have now found the next smallest (bottom leftmost) element, so we decriment k.
        k -= 1
        # If we have decrimented k times, we have found the kth smallest element
        if k == 0:
            return root.val
        # We have gone as far left as we can, so we will now go right one step and then
        # continue going left from there back in the while loop.
        root = root.right

# Make a binary search tree
'''
    4
   / \
  2   5
 / \   \
1   3   6
'''
node_dict = {}
for i in range(1,7):
    node_dict[i] = TreeNode(i)

node_dict[4].left = node_dict[2]
node_dict[4].right = node_dict[5]
node_dict[2].left = node_dict[1]
node_dict[2].right = node_dict[3]
node_dict[5].left = None
node_dict[5].right = node_dict[6]
node_dict[1].left = None
node_dict[1].right = None
node_dict[3].left = None
node_dict[3].right = None
node_dict[6].left = None
node_dict[6].right = None

print(kthSmallest(node_dict[4],3))

















