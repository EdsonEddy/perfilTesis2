casos=int(input())
if 1<=casos and casos<=50:
    while casos > 0:
        casos-=1
        x=int(input())
        if 1<=x and x<=50:
            l=[int(e) for e in input().split()]
            if len(l)==x:
               lor=sorted(l)
               s=" ".join([str(e) for e in lor])
               print(s,sep=" ",end="")
        print() 