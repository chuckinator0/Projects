'''
K-Messed Array Sort

Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

### Binary search tree method. Hard to implement in Python because it doesn't have a built-in data structure for it

'''
Basic plan:
1. create a binary search tree that is size k+1 (current element and then look at the next k upcoming elements) consisting of
	the first k+1 elements of the array
2. Set index = 0
3. pop the root of the BST (minimum value), update the arr[index], insert arr[index + k+1] into the BST (as long as index+k+1 < len(arr)),
	increment index
4. repeat step 3 until we go through the entire arr
5. return the arr

example:
input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
BST = 1->4->5

index = 0   arr = [(1), 4, 5, 2, 3, 7, 8, 6, 10, 9],  pop 1 from BST, update arr, insert arr[3], 2, into BST, giving 2->4->5
index = 1   arr = [(1), (2), 5, 2, 3, 7, 8, 6, 10, 9],  pop 2 from BST, insert arr[4], 3, into BST, giving 3->4->5
index = 2   arr = [(1), (2), (3), 2, 3, 7, 8, 6, 10, 9],  pop 3 from BST, insert arr[5], 7, into BST, giving 4->5->7
index = 3   arr = [(1), (2), (3), (4), 3, 7, 8, 6, 10, 9],  pop 4 from BST, insert arr[6], 8, into BST, giving 5->7->8
index = 4   arr = [(1), (2), (3), (4), (5), 7, 8, 6, 10, 9],  pop 5 from BST, insert arr[7], 6, into BST, giving 6->7->8
index = 5   arr = [(1), (2), (3), (4), (5), (6), 8, 6, 10, 9],  pop 6 from BST, insert arr[8], 10, into BST, giving 7->8->10
index = 6   arr = [(1), (2), (3), (4), (5), (6), (7), 6, 10, 9],  pop 7 from BST, insert arr[9], 9, into BST, giving 8->9->10
index = 7   arr = [(1), (2), (3), (4), (5), (6), (7), (8), 10, 9],  pop 8 from BST, don't insert, BST now 9-> 10
index = 8   arr = [(1), (2), (3), (4), (5), (6), (7), (8), (9), 9],  pop 9 from BST, don't insert, BST now 10
index = 9   arr = [(1), (2), (3), (4), (5), (6), (7), (8), (9), (10)],  pop 10 from BST, don't insert, BST now -
return arr

'''