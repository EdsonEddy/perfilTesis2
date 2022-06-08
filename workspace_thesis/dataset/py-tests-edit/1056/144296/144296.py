c=int(input())
for i in range(c):
    n=int(input())
    v=[n]
    for i in range(n):
        cad=input()
        v=list(map(int,cad.split()))
        #for i in range (1,len(v)):
        v.reverse()
        print(" ".join( repr(e) for e in v )+' ')
        break

