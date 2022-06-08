g=0
while g!="":
    g=int(input())
    a=input().split()
    l=[]
    for x in a:
        if x not in l:
            l.append(x)
        o=0
        for i in range(len(l)-1):
            k=a.count(l[i])
            o=o+k//2
    print(o)