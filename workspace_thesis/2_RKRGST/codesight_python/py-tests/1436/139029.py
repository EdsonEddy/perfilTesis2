a,b,c=input().split()
r=len(a)+len(b)+len(c)
res=""
if 0<=r<=15:
    li=[a,b,c]
    li.sort()
    for i in range(3):
        R=li[i]
        res=R+res
    print(res)