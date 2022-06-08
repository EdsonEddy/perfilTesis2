import sys
for x in sys.stdin:
    n=int(x)
    A = list( map(int,input().split()))
    B = list( map(int,input().split()))
    A.sort(reverse=True)
    B.sort()
    s=0
    for i in range (n):
        s=s + (A[i]*B[i])
    print (s)