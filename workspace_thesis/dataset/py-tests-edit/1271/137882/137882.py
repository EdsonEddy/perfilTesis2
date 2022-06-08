n=int(input())
for k in range(n):
    num=int(input())
    s=0
    mm=num
    while mm>0:
        j=mm%10
        ff=j
        f=1
        for i in range(j):
            f=f*ff
            ff=ff-1
        s=s+f
        mm=int(mm/10)
    if s==num:
        print("Y")
    else:
        print("N")