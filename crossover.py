from encode_decode import *
from freq_element import *
from check_spanning import *
def _crossover(s1,s2):
    s = ""
    n = len(s1)
    for i in range(0,n):
        a = int(s1[i])
        #print(type(s2[i]))
        b = int(s2[i])
        #print(type(b))
        a = a|b
        s = s+str(a)
    return s


#print(_crossover('1001','0000'))

def sortSecond(val):
    return val[1]
def crossover_sorting(s,graph):
    l=decode(s)
    #print("graph is {} and l {}".format(graph,l))
    l1=freq_element(create_subset_graph(graph,l))
    ans=[]
    for i in l:
        ans.append((i,l1[i-1]))
    # return ans
    ans.sort(key=sortSecond,reverse=True)
    l2=[]
    for i in ans:
        l2.append(i[0])
        if is_spanning_tree(graph,l2)== True:
            return l2
    return l2

def crossover(graph,s1,s2):
    s = _crossover(s1,s2)
    #print("crossover grah{}".format(graph))
    return crossover_sorting(s,graph)
    
#print(crossover(globals.graph,'1000','1001'))