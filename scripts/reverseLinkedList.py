'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# iterative
def reverseList(head):
	# check if the list is empty. If it is, return None
	if not head:
		return None
	else:
		current_node = head
		previous_node = None
		while current_node.next:
			# record the next node in the list
			next_node = current_node.next
			# reverse the direction of the list by pointing this node
			# back at the previous node
			current_node.next = previous_node
			# We have now processed the current node, so it becomes the previous node
			previous_node = current_node
			# After processing the current node, the next node we recorded earlier becomes the current node
			current_node = next_node
		# Once we get here, it means there is no next node, so we are at the 
		# end of the linked list. We must reverse the direction of this final node as well
		current_node.next = previous_node
		# return the final node, which is now the head of the reversed linked list
		return current_node


# Try a recursive approach
def reverseList2(node, previous = None):
	# If we get to the end of the linked list and go one further to None,
	# return the previous node which is the final node in the list
	if not node:
		return previous
	# assuming we aren't at the end, move to the next
	# node in the list, and redirect the next link to point backwards.
	# Note that the first item in the list will be redirected to None from
	# the default value of previous
	next_node, node.next = node.next, previous
	# In this recursive step, we go through the entire linked list, changing the
	# directions of the links along the way, until we reach the end of the list.
	# At that point, we hit the first clause and the end of the list is returned, which
	# is the beginning of the reversed list.
	return reverseList2(next_node, node)











