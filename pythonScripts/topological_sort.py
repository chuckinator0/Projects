'''
implement topological sort, which ensures an ordering of nodes so that no node is a parent of subsequent nodes.
This assumes the input is a directed acyclic graph. For testing whether a directed graph is acyclic, see
course_schedule.py
'''


def dfs(graph, node, sorted_stack, visited, unvisited):

	# Remove node from unvisited set and add it to visited set
	if node in unvisited:
		unvisited.remove(node)
	visited.add(node)

	# Reach to the depths of the graph to find leaves and nodes whose children have all been visited
	for neighbor in graph[node]:
		if neighbor not in visited:
			dfs(graph, neighbor, sorted_stack, visited, unvisited)

	# Only after adding all descendants to the sorted stack do we add this node to the sorted stack
	# If this node has no children or all its children have been visited, add it to the sorted stack
	if graph[node] == [] or [x for x in graph[node] if x in visited] == graph[node]:
		sorted_stack.append(node)

	return

def topo_sort(graph):

	unvisited = set()

	for node in graph:
		unvisited.add(node)

	visited = set()

	sorted_stack = []
	output_string = ''

	while unvisited:
		node = unvisited.pop()
		dfs(graph,node,sorted_stack,visited,unvisited)

	while sorted_stack:
		output_string += str(sorted_stack.pop(-1))

	return output_string

graph = {0:[1,2], 1:[2,3,4], 2: [3], 3: [], 4:[5], 5:[]}
graph2 = {5:[1,0], 1:[4,3], 2:[], 3:[2], 0:[], 4:[0]}

print(topo_sort(graph))


