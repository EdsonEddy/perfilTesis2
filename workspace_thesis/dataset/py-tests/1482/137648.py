n=int(input())
m=1
res=1
while m<=n:
    res*=m
    if m%2==1:
        print("-"+str(res))
    else:
        print(res)
    m+=1;