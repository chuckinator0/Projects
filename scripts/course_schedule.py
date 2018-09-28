'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

'''
To solve this problem, we'll create a directed graph where each node is a course and each directed edge from v to w
means that v is a prerequisite of w. Using depth first search, coming across a node that has already been visited means
there has been a cycle, which is the failure condition in this problem (we can't have two classes be prerequisites for each
other). However, DFS with directed graphs means we could only traverse a piece of the graph. We will need to keep a
global list of nodes that have been visited by various calls of DFS and only run DFS on nodes we haven't yet visited
globally.

Note also that we could do BFS as well if we assume cycles happen close to the root node. 
'''


def make_graph(numCourses, prerequisites):
	'''
	We are given a list of prerequisite pairs in the problem, but the object of interest we will be iterating over is the
	node. This function will take an the prereq list and produce a graph represented by a dictionary of the form
	{node: [list of nodes that can be reached from a directed edge from key node]}
	'''
	graph = {}

	for pair in prerequisites:
		# Each pair is [course, prerequisite], so our graph needs to make a directed edge
		# from the prerequisite to the course.
		if pair[1] in graph:
			graph[pair[1]].append(pair[0])
		else:
			graph[pair[1]] = [pair[0]]

	# We might have missed courses with no prerequisites, so let's add those into the dictionary
	for course in range(numCourses):
		if course in graph:
			continue
		else:
			graph[course] = []
	return graph

def detect_cycle(graph, node, visited, current_path, unvisited_nodes):
	'''
	This function recursively detects whether a cycle has occured on a single iteration depth first search
	'''
	# add node to visited set and remove it from unvisited
	visited.add(node)
	if node in unvisited_nodes:
		unvisited_nodes.remove(node)
	# add node to current path
	current_path.add(node)

	# recur for all neighbors
	# if any neighbor is visited AND in the current_path, then we have detected a cycle
	for neighbor in graph[node]:
		if neighbor not in visited:
			# if a cycle would be detected further down the path, then there has been a cycle
			if detect_cycle(graph, neighbor, visited, current_path, unvisited_nodes) == True:
				return True
		# at this point, we will have found a cycle if the neighbor has been visited and is in the current path
		elif neighbor in current_path:
			return True

	# if we haven't returned at this point, it means no cycles have been detected below node,
	# so we remove the node from the current path and signal no cycle has been detected below it
	current_path.remove(node)
	return False


def canFinish(numCourses, prerequisites):
	'''
	Take a number of courses (0 through n-1) and a list that describes the prerequisites, and return true if it's
	possible to finish the courses without a prerequisite cycle, and false if a cycle of prerequisites makes it
	impossible to finish.
	'''
	unvisited_nodes = set() # keep a global set of nodes that haven't been visited
	visited = set() # keep set of visited nodes
	current_path = set() # initialize current path, which will change as detect_cycle recurses
	
	graph = make_graph(numCourses, prerequisites)

	# Add all courses (nodes) to unvisited set
	for course in range(numCourses):
		unvisited_nodes.add(course)

	while unvisited_nodes:
		node = unvisited_nodes.pop()
		if detect_cycle(graph, node, visited, current_path, unvisited_nodes):
			return False # if a cycle is detected, then it's impossible to finish the courses

	# If we have survived the process of detecting cycles for each component of the graph, then there are
	# no cycles and it's possible to finish the courses.
	return True



print(canFinish(3, [[1,0],[2,0], [0,1]]))






