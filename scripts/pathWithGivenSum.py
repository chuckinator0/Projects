#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    if t:
        if not (t.left or t.right) and s == t.value:
            return True
        elif hasPathWithGivenSum(t.left, s - t.value):
            return True
        elif hasPathWithGivenSum(t.right, s - t.value):
            return True
        else:
            return False
    else:
        return False