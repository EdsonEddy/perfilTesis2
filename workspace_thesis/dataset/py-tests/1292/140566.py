import sys
def contar(n,s):
    v=s.split()
    x=0
    for i in range(len(v)):
        x=x+int(v[i])
    return x 

while True:
    n=int(input())
    s=input()
    r=contar(n,s)
    print(r)
