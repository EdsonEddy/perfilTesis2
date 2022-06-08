while 1:
    n=int(input())
    for k in range(n):
        p,n1= map(int,input().split())
        l = []
        for j in range(n1):
            l.append(1)
        lr=p-n1+1
        for w in range(lr):
            s = 0
            for x in range(w,len(l),1):
                s=s+l[x]
            l.append(s)
        print(l[p])
