import math
cad=0

def bin(x):
    global cad
    if x==0:
        return str(cad)
    e = int(math.log(x, 2))
    cad=cad+(10**e)
    return bin(x-(2**e))
n=int(input())
for i in range(n):
    x=int(input())
    c=0
    x=bin(x)
    cad=0
    while x.find("11")!=-1:
        x=x[(x.find("11"))+2:]
        c+=1
    print(c)
