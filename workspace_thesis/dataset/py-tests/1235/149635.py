n=int(input())
A=list(map(int,input().split()))
s=0
d=0
for i in range (len(A)):
   d+=A[i]
f=d
for i in range (n-1):
    s+=A[i]
    d-=A[i]
    e=d-s
    if(0<e<f):
        f=e
print(f)