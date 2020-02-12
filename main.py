from freq_element import *
from check_spanning import *
from collections import defaultdict
from mutation import *
import random
import globals
from crossover import *
from fitness import fitness 


solution = [0]*10000000
max_val = (2**(globals.no_of_labels))-1
fitness_val = 100000000
#print('max val ={}'.format(max_val))
b = random.randrange(1,max_val)
for i in range(0,globals.no_of_iterations):
  a= random.randrange(1,max_val)
  #print("values of a and b are {} {}".format(a,b))
  a = binary(a,globals.no_of_labels)
  b = binary(b,globals.no_of_labels)
  #print(a,b)
  a = str(a)
  b = str(b)
  #print(a,b)
  s = crossover(globals.graph,a,b)
  s = str(encode(s))
  """print("encode s {}".format(s))
  print("devesh")
  print(s)
  print("mut starts")"""
  #print("after crossover {}".format(s))
  t = mutation(globals.graph,s)
  """print("after mutation {}".format(t))
  print("mut ends")"""
  x = fitness(t)
  s2=t 
  if len(solution)>len(s2):
    solution = s2
    fitness_val = len(s2)
    b=s2
  b = s2  
  
  b = encode(b)
  #print("b is {}".format(b))
  b = bin_to_dec(b)
  a = bin_to_dec(a)
  print("values after {} iteration is {} and {} with fitness= {}".format(i,a,b,fitness_val))


#print(mutation(graph,'1001'))
#print(globals.graph)
#print(create_subset_graph(globals.graph,[1,3,4]))
