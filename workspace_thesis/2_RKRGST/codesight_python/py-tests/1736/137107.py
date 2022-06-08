N=int(input())
c=0
while (N>0):
    f=2**(2**c)+1
    c=c+1
    N=N-1
    print f,