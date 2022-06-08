x=int(input())
n,d=1,1
while n<=x:
    print(str(n)+"/"+str(d))
    if d==x:
        n+=1
        d=1
    else:
        d+=1