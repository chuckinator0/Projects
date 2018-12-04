"""
You need to climb a staircase that has n steps, and you decide to get some extra exercise
by jumping up the steps. You can cover at most k steps in a single jump. Return all the
possible sequences of jumps that you could take to climb the staircase, sorted.

Example

For n = 4 and k = 2, the output should be

climbingStaircase(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time.
There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.
"""
    
def climbingStaircase(n,k):
    
    # The main idea is to get the new ways to get up the stairs from the old ways.
    # We look at the solution from one step back and append a 1-hop,
    # then look back two steps and append a 2-hop, etc, until we
    # look back k steps and do a k-hop.
    
    def compute_new_ways(current_step,k,memo):
        # given the current step and the memo of precomputed values,
        # return a list of the ways to get to the current step (list of lists)
        ways = []
        for j in range(1, min(current_step,k)+1):
            for way in memo[current_step - j]:
                copy = way.copy()
                copy.append(j)
                ways.append(copy)
        return sorted(ways)
    
    memo = {0:[[]]} # {step: [ways to get to step]}
    
    for current_step in range(1,n+1):
        memo[current_step] = compute_new_ways(current_step,k,memo)
    
    return memo[n]

# This code can be optimized to use a memo of size k rather than a memo of size n
# since we only need to look back at most k steps.

print(climbingStaircase(4,3))