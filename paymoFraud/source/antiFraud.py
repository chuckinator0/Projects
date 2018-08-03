##### Introduction

## This program aims to prevent fraudulent payment requests from untrusted
## users.  There are three features with increasing thresholds for verifying
## payment requests:
##
## Feature 1 - A payment request is considered unverified if the user has never
## interacted with the requestor before.
##
## Feature 2 - A payment request is considered unverified if the user has more
## than two degrees of separation with the requestor.
##
## Feature 3 - A payment request is considered unverified if the user has more
## than four degrees of separation with the requestor.
##
## The program is organized as follows:
## 1. Data and Initialization
## 2. Functions
## 3. Main Program
## 4. Output


##### Data and Initialization

## Import modules, data from files, and create variables and data structures
## that will be used in the main program.

import csv
import queue

# Initialize a graph whose nodes represent user id's and whose edges represent
# transactions.  The data structure is a dictionary { node : set of edges }
# which will efficiently test whether two nodes are connected.  The use of sets
# ensures that edges can be added multiple times without introducing redundant
# edges.
user_graph = {}

# Ignore emojis that will throw errors when opening the csv.
# The data has header { time, id1, id2, amount, message }.
with open('../input/testCSV.csv','r', errors = 'ignore') as testCSV:
    data = csv.DictReader(testCSV)
    # initialize nodes as id's and edge sets with the empty set.
    for row in data:
        id1 = int(row[' id1'])
        id2 = int(row[' id2'])
        user_graph[id1] = set([])
        user_graph[id2] = set([])
    # return to the beginning of the data and skip the header row.
    testCSV.seek(0)
    next(data)
    # initialize edges. For each transaction,
    # add id1 to the edge set of id2 and vice versa.
    for row in data:
        id1 = int(row[' id1'])
        id2 = int(row[' id2'])
        user_graph[id1].add(id2)
        user_graph[id2].add(id1)


##### Functions

## Define any functions that the main program requires.
## Calculations that need to be repeated at different points of a program
## should be coded as functions.

# isFriend takes inputs: a graph, a sourceNode, a checkNode, and an integer k.
# The graph is a dictionary { nodes : set of edges }.
# The sourceNode is the user id.
# The checkNode is the user id making a request that needs to be verified.
# The integer k represents the maximum distance from checkNode to sourceNode
# as determined by the desired feature.
#
# If the distance from checkNode to sourceNode is greater than k,
# then isFriend returns False, denoting the requestor is unverified.
#
# If the distance from checkNode to sourceNode is less than or equal to k,
# then isFriend returns True, denoting a verified transaction.

def isFriend(graph, sourceNode, checkNode, k ):
    # dist encodes { node id : distance to source } and
    # visited {node id: True/False} encodes whether a node has already been
    # visited.
    dist = {sourceNode: 0}
    visited = {}

    # Enqueue the source node, which has distance 0 from itself.
    friendQueue = queue.Queue()
    friendQueue.put(sourceNode)
    
    # Traverse the graph outward from source node until reaching a node
    # with distance greater than k from the source.
    while not friendQueue.empty():
        u = friendQueue.get()
        if dist[u] < k:
            # for each neighbor in the edge set of u that hasn't been visited,
            # add it to dist with distance increased by 1 from predecessor
            # and mark it as visited.
            for neighbor in graph[u]:
                if visited.get(neighbor) == None:
                    dist[neighbor] = dist[u] + 1
                    visited[neighbor] = True
                    friendQueue.put(neighbor)
        else:
            break

    # If the checkNode has been visited, then the requestor is verified and
    # isFriend returns true.
    if checkNode in visited:
        return True
    else:
        return False



##### Main Program

## Perform relevant computations, using functions as needed

# Run Feature 1
k = 1

outfile = open('../output/output1.txt', "w")
with open('../input/streamCSV.csv','r', errors = 'ignore') as streamCSV:
    stream = csv.DictReader(streamCSV)
    for row in stream:
        id1 = int(row[' id1'])
        id2 = int(row[' id2'])
        if isFriend(user_graph, id1, id2, k):
            outfile.write('verified\n')
        else:
            outfile.write('unverified\n')
outfile.close()

# Run Feature 2
k = 2

outfile = open('../output/output2.txt', "w")
with open('../input/streamCSV.csv','r', errors = 'ignore') as streamCSV:
    stream = csv.DictReader(streamCSV)
    for row in stream:
        id1 = int(row[' id1'])
        id2 = int(row[' id2'])
        if isFriend(user_graph, id1, id2, k):
            outfile.write('verified\n')
        else:
            outfile.write('unverified\n')
outfile.close()

# Run Feature 3
k = 4

outfile = open('../output/output3.txt', "w")
with open('../input/streamCSV.csv','r', errors = 'ignore') as streamCSV:
    stream = csv.DictReader(streamCSV)
    for row in stream:
        id1 = int(row[' id1'])
        id2 = int(row[' id2'])
        if isFriend(user_graph, id1, id2, k):
            outfile.write('verified\n')
        else:
            outfile.write('unverified\n')
outfile.close()
