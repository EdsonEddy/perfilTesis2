c=int(input())
for i in range(c):
    a,b=map(int,input().split())
    l=input().split()
    la=l[a:b+1]
    s=0
    for j in la:
        s=s+int(j)
    print(s)