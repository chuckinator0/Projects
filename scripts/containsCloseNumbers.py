'''
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

Example

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
containsCloseNums(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
containsCloseNums(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.
'''
from collections import defaultdict
def containsCloseNums(nums, k):
    
    index_dict = defaultdict(list) # { number: list of indices where that number occurs in nums }
    
    for index, num in enumerate(nums):  
        if num not in index_dict:
            index_dict[num].append(index)
        elif index - index_dict[num][-1] <= k:
                return True
        else:
            index_dict[num].append(index)
    
    return False

print(containsCloseNums([0, 1, 2, 3, 5, 2],3)) # expect true