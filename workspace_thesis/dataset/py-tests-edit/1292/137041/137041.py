s=True
while s == True:
    c=0
    n=int(input())
    if n!=0:
        dato=list(map(int,input().split()))
        for i in range(n):
            if dato[i]!=0:
                c=c+dato[i]
        print(c)
    else:
        s=False
        break
