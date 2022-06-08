while True:
    a=int(input())
    lh=list(map(int,input().split()))
    ln=list(map(int,input().split()))
    s=0
    h=0
    for i in range(a):
       s=s+lh[i]+ln[i]
       p=s/a
    for j in range(a):
       if lh[j]+ln[j]<p:
           h=h+1
    print(h)