import sys
def contar(n,s):
    v=s.split()
    x=0
    for i in range(len(v)):
        x=x+int(v[i])
    return x 

for n in sys.stdin:
    n=int(n)
    s=input()
    r=contar(n,s)
    print(r)
