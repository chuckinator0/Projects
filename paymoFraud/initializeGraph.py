import csv

# Initialize graph from database csv
user_graph = {}
with open('testCSV.csv','r', errors = 'ignore') as testCSV:
    data = csv.DictReader(testCSV)
    # initialize nodes
    for row in data:
        id1 = int(row[' id1'])
        id2 = int(row[' id2'])
        user_graph[id1] = set([])
        user_graph[id2] = set([])
    testCSV.seek(0)
    next(data)
    # initialize edges
    for row in data:
        id1 = int(row[' id1'])
        id2 = int(row[' id2'])
        user_graph[id1].add(id2)
        user_graph[id2].add(id1)

print(user_graph)



