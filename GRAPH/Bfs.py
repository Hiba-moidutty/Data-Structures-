graph = {}

def addnode(v):
    if v in graph:
        print(v,"is already present")
    else:
        graph[v] = []
        

def addedge(v1,v2):
    if v1 not in graph:
        print(v1,"not present")
    elif v2 not in graph:
        print(v2," not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
        
def delnode(v):
    if v not in graph:
        print(v,"not present")
    else:
        graph.pop(v)
        for i in graph:
            l = graph[i]
            for v in l:
                l.remove(v)
  
        
def deledge(v1,v2):
    if v1 not in graph:
        print(v1,"not present")
    elif v2 not in graph:
        print(v2,"not present")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
        
        
def BFS(node,graph):
    visited = set()
    if node not in graph:
        print("node not in graph")
        return 
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current,"->",end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)
#     for i in graph:
#         if i not in visited:
#             print(i,"->",end=" ")
           
        
        
addnode(4)
addnode(10)
addnode(12)
addnode(5)
addnode(8)
addnode(2)
addedge(2,10)
addedge(4,10)
addedge(12,4)
addedge(12,8)
addedge(8,4)
addedge(4,5)
addedge(8,10)
deledge(12,4)
print(graph)
print("\n\nBFS traversal")
BFS(8,graph)