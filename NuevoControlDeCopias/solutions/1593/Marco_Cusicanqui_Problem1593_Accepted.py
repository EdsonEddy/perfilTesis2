import sys

# 2*5, 10=2*5,
# 5, 10, 15, 20, 25=5*5, 30=5*6,
# 5*2, 5*2, 5*2, 5*2 ...
# 5, 10, 15, 20, 25, 30
v=[]
curr=5
cnt=0
while cnt<=100000:
    x=curr
    while x%5==0:
        cnt+=1
        x//=5
    curr = curr + 5
    v.append((curr-5,cnt))

cin=sys.stdin
for line in cin:
    x=int(line)
    lo,hi=0,len(v)
    while lo+1 != hi:
        mid=(lo+hi)//2
        if v[mid][1]<=x: lo=mid
        else: hi=mid
    if v[lo][1]!=x: print(0)
    else:
        for i in range(v[lo][0], v[lo+1][0]):
            if i<v[lo+1][0]-1: print(i,end=' ')
            else: print(i)

