import heapq
def kthLargestElement(nums, k):
    '''
    select the kth largest element in a list. We split the input into two heaps:
    a max heap of size len(nums)-k on the left and a minheap of size k on the right.
    We rebalance the two heaps until every element of the left heap is less than
    every element of the right heap. Once the heaps are rebalanced, the kth largest element is
    the smallest element of the right heap.

    We could also solve this problem with quickselect, but heaps are fun too!
    '''
    def rebalance(leftheap,rightheap):
        '''
        While any element in the left heap is greater than the smallest element
        in the right heap, swap those elements with each other.
        '''
        # it could be possible for the left heap to be empty, in which case no rebalancing
        # is necessary
        if not leftheap:
            return
        # note here the negative due to how heapq requires us to implement max heaps as min heaps
        # with negative values
        while -leftheap[0] > rightheap[0]:
            # note the negative
            right_to_left = -heapq.heappop(rightheap)
            # again note the negative
            left_to_right = -heapq.heappop(leftheap)
            heapq.heappush(rightheap,left_to_right)
            heapq.heappush(leftheap,right_to_left)
        return
    
    # initialize max heap of size len(nums)-k for the left heap. Note that with
    # heapq, the standard way to make a max heap is to make a minheap of negative values.
    leftheap = [-num for num in nums[:len(nums)-k]]
    # initialize min heap of size k for the right heap
    rightheap = nums[-k:]
    heapq.heapify(leftheap)
    heapq.heapify(rightheap)
    
    rebalance(leftheap,rightheap)
    return heapq.heappop(rightheap)

print(kthLargestElement([-1,-2,-3],2))