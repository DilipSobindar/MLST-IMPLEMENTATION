import numpy as np 
import globals 
from collections import defaultdict
def freq_element(graph):
    #print("subset graph {}".format(graph))
    l = np.zeros(globals.no_of_labels,dtype=int)
    for nodes in graph:
        for neighbour,key in graph[nodes]:
            l[key-1]+=1
    return (l//2)
def dict_create(graph):
    dict = defaultdict(int)
    for nodes in graph:
        dict[nodes]=0
    return dict

#print(freq_element(globals.graph))
