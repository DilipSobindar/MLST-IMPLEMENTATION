from encode_decode import encode,decode
from freq_element import *
from collections import defaultdict
from check_spanning import *
graph = {
          'a': {'b': 1, 'e': 4,'c':2},
          'b': {'a':1,'c':  3, 'd':3, 'e':4},
          'c': {'a':2,'d':1,'b':3},
          'd': {'b':3,'e':1, 'c':1},
          'e': {'d':1,'a':4,'b':4}
        }
def _mutation(s):
    n = len(s)
    if s[0]=='0':
        return '1'+s[1:]
    
    for i in range(0,n-1):
        if s[i]=='0':
            s = s[:i]+'1'+s[i+1:]
            return s
    if s[n-1]=='0':
        return s[:n-1]+'1'
    return s
    
def sortSecond(val):
    return val[1]
def mutation_sorting(s,graph):
    #print("s is {}".format(s))
    l=decode(s)
    #print("labels is {}".format(l))
    #print(graph)
    z =create_subset_graph(graph,l)
    #print("z {}".format(z))
    l1=freq_element(z)
    #print("l1 value{}".format(l1))
    ans=[]
    for i in l:
        ans.append((i,l1[i-1]))
    # return ans
    ans.sort(key=sortSecond,reverse=True)
    l2=[]
    for i in ans:
        l2.append(i[0])
    return l2

def label_remove(graph,label):
    count = len(label)
    x=0
    while x<count:
        q = label.pop()
        if is_spanning_tree(graph,label)==True:
            continue
        else:
            label.insert(0,q)
        x+=1
    return label



#print(mutation('1010'))
#print(mutation_sorting('1010',graph))

#print(label_remove(graph,mutation_sorting('1010',graph)))
def mutation(graph,s):
    s = _mutation(s)
    #print("_mutation {}".format(s))
    #print("mutation sorting called")
    x = mutation_sorting(s,graph)
    #print("till")
    #print("x = {}".format(x))
    return label_remove(graph,x)


