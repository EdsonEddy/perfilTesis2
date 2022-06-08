n=str(input())
for i in n:
    a=ord(i)
    r=bin(a)
    res=r[2::].zfill(8)
    print(res,end="")