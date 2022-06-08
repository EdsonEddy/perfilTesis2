while 1:
    n=int(input())
    c=input().split()
    ce=c[:n]
    b=[int(x) for x in ce]
    b.sort()
    c=0
    k=0
    while k<len(b):
        if k+1<len(b):
            if b[k]==b[k+1]:
                c=c+1
                k+=1
        k+=1
    print(c)