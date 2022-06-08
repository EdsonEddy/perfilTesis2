import sys
def leeVector(n):
    global A
    x=input()
    A=x.split(" ")
    return A

def repetido(A,n):
    c=0
    for i in range(n):
        if A[i]==A[n-1]:
            c=c+1
    return c

for n in sys.stdin:
    n=int(n)
    A=[]
    leeVector(n)
    r1=repetido(A,n)
    print(r1)