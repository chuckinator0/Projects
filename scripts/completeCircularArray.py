'''
Write a function that returns true if the circular array of relative indicies cycles completely.
For example, the array [2,2,-1] would return true, since we go from index 0 (forward 2 mod 3) to index 2, then back (-1 mod 3) to index 1, and then forward
(2 mod 3) to get back to index 0. We have visited all indicies and returned to the starting index.
'''

def isCompleteCircular(array):
  n = len(array)
  visited = set()
  index = 0
  count = 0
  while count < n:
    next_index = (index + array[index]) % n
    if next_index in visited:
      return False
    else:
      visited.add(next_index)
      index = next_index
      count += 1
  return True

testlist = [ [2,3,-1], [3,3,3], [5,-4,-1], [2,2,-1,1], [2,2,-1,-1], [], [2], [-3,5,1,1]  ]
expected_outputs = [False, False, True, True, False, True, True, True ]

def test_isCompleteCircular(testlist, expected_outputs):
  if len(testlist) != len(expected_outputs):
    return "Error: testlist and expected output list are different lengths"
  for i in range(len(testlist)):
    if isCompleteCircular(testlist[i]) != expected_outputs[i]:
      return f"The input {testlist[i]} was expected to return {expected_outputs[i]}"
  return "all tests passed"

print(test_isCompleteCircular(testlist,expected_outputs))
