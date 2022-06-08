g=int(input())
for h in range(g):
    a,b= map(int,input().split())
    c=input().split()
    d=c[a:b+1]
    f=0
    for e in d:
        e=int(e)
        f=f+e
    print(f)