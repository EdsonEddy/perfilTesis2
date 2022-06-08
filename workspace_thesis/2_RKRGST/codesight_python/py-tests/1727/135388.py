l, r, k=map(int, input().split(" "))
c=0
if l > r:
    while l >= r:
        if (r %k)==0:
            c=c+1
        r =r+1
else:
    while l <= r:
        if (l %k)==0:
            c=c+1
        l=l+1
print(c)
    
