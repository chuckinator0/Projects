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
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

## For fun, check to see if we can just use quick select here (see quickselect.py)
# from quickselect import quickselect

# def kthSmallest(root,k):
#   for element in root:
#     if element is None:
#       root.remove(element)
#   return quickselect(root,k)


# Yay, it works! But it's only valid if we are given the binary tree in array form.


# Let's try using treeNode objects
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = [3,1,4,None,2]
k=1

print(kthSmallest(root,k))
