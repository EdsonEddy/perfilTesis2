n=int(input())
for i in range(n):
    r=0
    a,b,c=map(int,input().split())
    d=input().split()
    l=d[b:c+1]
    for y in range(len(l)):
        r=int(l[y])+r
    print(r)