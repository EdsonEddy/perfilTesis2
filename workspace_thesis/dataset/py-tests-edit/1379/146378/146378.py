g=""
while g!=0:
    g=int(input())
    x=input().split()
    x.sort()
    c=""
    for i in range(len(x)-1,-1,-1):
        c=c+x[i]
    print(c)