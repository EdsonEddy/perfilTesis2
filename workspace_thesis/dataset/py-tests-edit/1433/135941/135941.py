a,b=map(int,input().split())
k=2
p=a
cp=0
while a<=b:
    p=a
    if p!=1:
        while p%k != 0 and k <= p//2:
            k+=1
        if k > p//2:
            cp+=1
    a+=1
    k=2
print(cp)