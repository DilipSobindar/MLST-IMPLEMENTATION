from freq_element import dict_create
from collections import defaultdict
#dict = dict_create(graph)


def create_subset_graph(graph,labels):
    dict = defaultdict(list)
    for nodes in graph:
        for neighbours,key in graph[nodes]:
            if key in labels:
                dict[nodes].append((neighbours,key))
                #dict[neighbours].append((nodes,key))
    return dict

def dfs(graph,visited,node):
    #print(node,graph[node],visited[node])
    visited[node]=1
    #print(node,graph[node],visited[node])
    for neighbours,key in graph[node]:
        #print(node,neighbours)
        if visited[neighbours] == 0:
            dfs(graph,visited,neighbours)
        
def checkz(visited):
    for key in visited:
        if visited[key]==0:
            return False
    return True

def is_spanning_tree(graphs,labels):
    g = create_subset_graph(graphs,labels)
    visited = dict_create(graphs)
    dfs(g,visited,'a')
    return checkz(visited)
