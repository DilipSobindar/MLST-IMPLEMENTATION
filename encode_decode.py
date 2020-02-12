def decode(s):
    l = []
    n = len(s)
    for i in range (0,n):
        if s[i]=='1':
            l.append(n-i)
    return l

def encode(l):
    s=[]
    for i in range(max(l)):
        s.append('0')
    for i in l:
        s[i-1]='1'
    s=s[::-1]
    k = ''
    for i in s:
        k+=i
    return k
    
def binary(a,sz):
    a = bin(a)
    a= str(a)
    a = a[2:]
    while len(a)<sz:
        a = '0'+a
    return a
#print(binary(11,4))
def bin_to_dec(a):
    val=0
    b = ''.join(reversed(str(a)))
    for i in range(0,len(b)):
        val = val + int(b[i])* (2**i)
    return val 
"""print(encode({1, 4, 8, 9}))
print(decode('1011'))"""
#print(bin_to_dec('0001001'))