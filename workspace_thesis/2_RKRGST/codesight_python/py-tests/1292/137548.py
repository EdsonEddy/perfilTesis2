sw=True
while sw==True: 
    h=0
    g=int(input())
    if g!=0:
        m=list(map(int,input().split()))
        for i in range(g):
            if m[i]!=0:
                h=h+m[i]
        print(h)
    else:
        if g==0:
            sw=False
            break