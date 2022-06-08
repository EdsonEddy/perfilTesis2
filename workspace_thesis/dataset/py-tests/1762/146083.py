while True:
    q=int(input())
    l=list(map(int,input().split()))
    l.sort()
    a,b=int(0),int(0)
    w=l[:q]
    while b<len(w)-1:
        if w[b]==w[b+1]:
            a+=1
            b+=2
        else:
            b+=1
    print(a)

