def suma(y):
    res=0
    for i in range(len(v)):
        res+=int(v[i])
    return res
from sys import*
for line in stdin:
    v=line.split()
    print(suma(v))