n=int(input())
x=0
for i in range(0,n,1):
    e=2**i
    r=(2**e)+1
    if i==n-1:
        print(r)
    else:
       print(r,end=" ")