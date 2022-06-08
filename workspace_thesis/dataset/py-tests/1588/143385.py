k=int(input())
for j in range(1,k+1,1):
    h=0
    g=int(input())
    if g!=0:
        m=list(map(int,input().split()))
        for i in range(g):
            if m[i]%3==0:
                m[i]=m[i]*2
                h=h+m[i]
        print("La suma es",str(h))
   