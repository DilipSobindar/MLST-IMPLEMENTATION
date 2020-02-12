from freq_element import *
from check_spanning import is_spanning_tree
from collections import defaultdict
from mutation import *
"""graph = { "a" : [("c",2),("e",1),("b",1)],
          "b" : [("a",1), ("d",1)],
          "e" : [("a",1),("c",2), ("f",3)],
          "d" : [("b",1),("f",2)],
          "c" : [("a",2),("e",2),("f",3)],
          "f" : [("d",2),("e",3),("c",3)]
        }"""
graph =  defaultdict(list)
graph = {
          'a': {'b': 1, 'e': 4,'c':2},
          'b': {'a':1,'c':  3, 'd':3, 'e':4},
          'c': {'a':2,'d':1,'b':3},
          'd': {'b':3,'e':1, 'c':1},
          'e': {'d':1,'a':4,'b':4}
        }
print(graph['b']['c'])
print(type(graph))
      

#encode_decode(no_of labels)

#sort according to freq 
#print(mutation('1001',graph))
print(is_spanning_tree(graph,{4,3}))
#print(freq_element(graph))
