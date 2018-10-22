'''
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.
'''


#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def mirror(s,t):
    # let's look at situations when at least one node is None
    if not (s and t):
        # Two empty trees are mirrors of each other
        if not s and not t:
            return True
        # if one is None and the other exits, then the trees are not symmetric
        else:
            return False
    # Let's look at when both nodes exist. In order for the trees to be symmetric,
    # the root values must be equal, and
    elif s.value == t.value:
        # the left subtree of s must be a mirror of the right subtree of t, and visa versa
        return mirror(s.left,t.right) and mirror(s.right,t.left)
    
    else:
        return False
    

def isTreeSymmetric(t):
    if not t:
        return True
    return mirror(t.left,t.right)