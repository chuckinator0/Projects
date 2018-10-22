'''
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber
that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python),
assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr.
If successful and still have time, see if you can come up with an algorithm with an
improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Example:

input:  arr = [0, 1, 2, 3]

output: 4 
'''

def get_different_number(arr):
  # create a set for efficient membership checking
  mySet = set(arr)
  # start checking numbers from 0
  number = 0
  # In the worst case, our array is [0,1,2,...,n-1] and we return n. If the array contains numbers greater than
  # n, then it will be missing a number in the set [0,n-1]. So we just iterate number on 0,...,n-1
  while number < len(arr):
    if number not in mySet:
      return number
    number += 1
  # If we survive to here, it means the array was [0,1,2,...,n-1], and so the smallest value not in the list is n.
  return len(arr)


'''
Some commentary. Here, making a set is O(n) time, and finding the minimum value not in the list is at worst O(n)
time. This does require storing the set, which is O(n) space.

If we valued space more than time, we could get O(nlogn) time complexity with O(1) space complexity. First,
we sort the list. Then, the first element that doesn't come directly after the previous element tells us that we
skipped one or more elements, so we return one greater than the previous.
'''

def getDiff(arr):
  arr.sort()
  for index, element in enumerate(arr):
    # after sorting, the element and the index should match. If they don't, it means we skipped a number.
    # That's the minimum number not in the array, so we return it.
    if element != index:
      return arr[index-1] + 1
  # If we survive the for loop, it means the array was [0,1,2,...,n-1], so we return n.
  return len(arr)



def get_different_number(arr):
  mySet = set(arr)
  number = 0
  while number < len(arr):
    if number not in mySet:
      return number
    number += 1
  return len(arr)

test = [5,20,2,1,3,5,0,6,7,20]
test1 = [0,1,2,3]
print(get_different_number(test))
print(getDiff(test))