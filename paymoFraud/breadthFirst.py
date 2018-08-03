## Breadth-first search algorithm to determine degree of friendship.  Choose
## a source node and move outwards, labeling adjacent nodes with distance
## 1. Repeat to label friends of friends distance 2, etc.

import queue

# Feature 1: warn user if transaction partner is not a friend (k > 1)

# Feature 2: warn user if transaction partner is not at least a friend of a
# friend (k > 2)

# Feature 3: warn user if transaction partner has k > 4


def isFriend(graph, sourceNode, checkNode, k ):
    # friendInfo encodes {node id: distance to source}
    dist = {sourceNode: 0}
    firendQueue = queue.Queue()
    friendQueue.put(sourceNode)

    while not friendQueue.empty():
        u = friendQueue.get()
        if dist[u] < k:
            for neighbor in graph[u]:
                dist[neighbor] = dist[u] + 1
                friendQueue.put(neighbor)
        else:
            break

    if checkNode in dist:
        return True
    else:
        return False



### Testing the distance and predecessor attributes
##listy = [1,2,3,4,5]
##listy[3] = {'distance': 5, 'predecessor': 1}
##listy[2] = {'distance': 100, 'predecessor': 14}
##print(listy[3]['distance'])
##print(listy[2]['predecessor'])

### Testing queues
##q = queue.Queue()
##q.put(5)
##q.put(6)
##print(q.get())
