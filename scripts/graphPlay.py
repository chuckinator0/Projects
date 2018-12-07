'''
Just playing around with graphs and classes and stacks and queues and stuff.
Nodes in a directed graph have values and children, a possibly other properties based on the situation.
'''

from queue import Queue
# .put() to put things in the queue and .get() to pop from the queue

class Node:
	def __init__(self, value = 0, children = [], visited = False, ID = None):
		self.value = value
		self.children = children
		self.visited = visited
		self.ID = ID


# Let's manually build a graph. Create 10 nodes and keep an id for each node in this graph dictionary.
graph = {ID : Node() for ID in range(10)}

def populate_graph(graph, node_ID, value, children):
	graph[node_ID].value = value
	graph[node_ID].children = children
	graph[node_ID].ID = node_ID

populate_graph(graph, 0, 5, [graph[1],graph[9]])
populate_graph(graph, 1, 9, [graph[2],graph[4]])
populate_graph(graph, 2, 7, [graph[3]])
populate_graph(graph, 3, 2, [graph[1]])
populate_graph(graph, 4, 3, [graph[5],graph[6],graph[7]])
populate_graph(graph, 5, 7, [])
populate_graph(graph, 6, 3, [])
populate_graph(graph, 7, 5, [graph[8]])
populate_graph(graph, 8, 8, [])
populate_graph(graph, 9, 1, [graph[8]])


def bfs(graph,root):
	# Let's do a breadth first search that prints when it visits each node.
	q = Queue()
	q.put(root)

	while q:
		current_node = q.get()
		current_node.visited = True
		print(f'We just visited node {current_node.ID}\n')
		for child in current_node.children:
			if not child.visited:
				q.put(child)

def dfs(graph,root):
	# Let's do a depth first search that prints when it visits each node.
	# Notice we don't visit a node twice, otherwise we would get caught in 
	# an infinite loop if there is a cycle in the directed graph.
	# We can actually use this DFS to detect cycles. See the "course schedule"
	# problem to see how to do that.
	stack = [root]

	while stack:
		current_node = stack.pop()
		current_node.visited = True
		print(f'We just visited node {current_node.ID}\n')
		if current_node.children:
			for child in current_node.children:
				if not child.visited:
					stack.append(child)




dfs(graph,graph[0])



	






