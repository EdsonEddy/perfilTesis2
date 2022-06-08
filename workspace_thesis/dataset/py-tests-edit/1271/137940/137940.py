n=int(input())
for i in range(n):
    x=int(input())
    res=0
    k=x
    while(x>0):
        dig=x%10
        x//=10
        aux=1
        for j in range(1,dig+1):
            aux*=j
        res+=aux
    if (res==k):
        print("Y")
    else:
        print("N")
