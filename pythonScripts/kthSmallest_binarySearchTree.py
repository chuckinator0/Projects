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


# We can keep in mind that in a Binary Search Tree, each node is greater than its
# left child and less than its right child.
def kthSmallest(root,k):
  pass

















