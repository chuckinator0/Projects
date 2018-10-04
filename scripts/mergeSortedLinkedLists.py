'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def mergeTwoLists(l1,l2):
	# I learned something here. We need to keep track of the head to return, so what we are
	# doing is creating a new "dummy" node at the beginning of the merged list we want to
	# return. The syntax here means both dummy_head and tail refer to the same node object.
	# The tail will get updated as we go through the lists, but the dummy head will remain
	# referenced to this dummy node.
	dummy_head = tail = ListNode(0)
	# We want to check that both these nodes exist so we can compare them.
	while l1 and l2:
		# whichever node has the least value becomes the next node in our
		# merged list
		if l1.val < l2.val:
			tail.next = l1
			# iterate one place on the first list
			l1 = l1.next
		else:
			tail.next = l2
			# iterate one place on the second list
			l2 = l2.next
		# iterate the tail to the next place in the merged list. Go back to the 
		# beginning of the loop and compare the next nodes in the list again
		tail = tail.next
	# At this point, one of the lists has ended and one of the nodes is a None object.
	# Set the tail equal to whichever node still exists. This appends the rest of the list for
	# the node that still exists. If both nodes are None, it means both lists were the same length
	# and (l1 or l2) returns None.
	tail.next = l1 or l2
	# The actual head of the new linked list starts after the dummy node we created at the beginning.
	head = dummy_head.next
	return head

