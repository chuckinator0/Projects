'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

# Faster
# I also decided that I don't like that the output cuts off elements even if
# their count is tied with another top_k element's count. So instead, I am
# going to output the top k counts along with the elements with those counts. 
def topKCounts(nums,k):
	# maintain a dictionary of the form {element of nums: count of element in nums}
	element_to_count = {}
	for element in nums:
		# if the element hasn't been encountered before, add it to the dictionary with a count of 1
		if element not in element_to_count:
			element_to_count[element] = 1
		# if the element is already in the dictionary, add 1 to its count
		else:
			element_to_count[element] += 1
	# maintain a dictionary of the form {count:[list of elements with count]}
	# Get the count from the element_to_count dictionary and add the element to
	# the list of elements with that count.
	count_to_elements = {}
	for (element,count) in element_to_count.items():
		if count in count_to_elements:
			count_to_elements[count].append(element)
		else:
			count_to_elements[count] = [element]
	# sort dictionary by count in descending order and return the top k counts.
	sorted_by_count = sorted(count_to_elements.keys())[::-1]
	top_k_counts = {k:count_to_elements[k] for k in sorted_by_count[:k]}
	return '{Count: List of elements with that count}\n' + str(top_k_counts)




# Slower version that sticks to original problem statement:

def topKFrequent(nums,k):
	# maintain a dictionary of the form {element of nums: count of element in nums}
	count_dict = {}
	for element in nums:
		# if the element hasn't been encountered before, add it to the dictionary with a count of 1
		if element not in count_dict:
			count_dict[element] = 1
		# if the element is already in the dictionary
		else:
			count_dict[element] += 1
	# now we maintain a top_k list of the form [elements with greatest counts in descending order by count] of size k
	top_k = [None]*k
	# set a threshhold for entry into the top_k list
	current_threshhold = 0

	# populate top_k list
	for element in count_dict:
		if count_dict[element] > current_threshhold:
			for index in range(k):
				# if there is a None entry in top_k, we insert the element before it and remove the last element to
				# keep top_k size k.
				if top_k[index] is None:
					top_k.insert(index,element)
					del top_k[-1]
					# break here because we have found a spot for element in top_k
					break
				# compare the count of the element to the count of the item currently in top_k.
				# If the count of the element is greater or equal, insert it into the list and remove the last
				# element of top_k.
				elif count_dict[element] >= count_dict[top_k[index]]:
					top_k.insert(index,element)
					del top_k[-1]
					# break here because we have found a spot for element in top_k
					break
			# If there is a last element of top_k, the threshhold will be the count of that element.
			# If the last element of top_k is still None, then we will just continue to pupulate top_k
			if top_k[-1]:
				current_threshhold = count_dict[top_k[-1]]

	return top_k

# Just for fun, let's do a top k most frequent elements where there can be
# lots of ties and those are included in the output list instead of truncating
def topKFrequentFull(nums,k):
	# maintain a dictionary of the form {element of nums: count of element in nums}
	element_to_count = {}
	for element in nums:
		# if the element hasn't been encountered before, add it to the dictionary with a count of 1
		if element not in element_to_count:
			element_to_count[element] = 1
		# if the element is already in the dictionary, add 1 to its count
		else:
			element_to_count[element] += 1
	# maintain a dictionary of the form {count:[list of elements with count]}
	# Get the count from the element_to_count dictionary and add the element to
	# the list of elements with that count.
	count_to_elements = {}
	for (element,count) in element_to_count.items():
		if count in count_to_elements:
			count_to_elements[count].append(element)
		else:
			count_to_elements[count] = [element]
	# output top_k list, including
	index = 0
	top_k = []
	sorted_by_count = sorted(count_to_elements.keys())[::-1]
	for count in sorted_by_count:
		if index >= k:
			break
		else:
			top_k.extend(count_to_elements[count])
	return top_k


arr = [1,1,1,2,2,2,2,2,3,4,3,4]
k = 3
print(topKFrequent(arr,k))
print(topKFrequentFull(arr,k))
print(topKCounts(arr,k))

