n=0
while n!="":
    n=int(input())
    u=list(range(1,n))
    to=set(u)
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    lisx=[a,b,c]
    lisy=[x,y,z]
    cx=set(lisx)
    cy=set(lisy)
    px=cx&to
    py=cy&to
    uno=len(px)
    dos=len(py)
    r=(uno+1)*(dos+1)
    print(r)
    
