cas=int(input())
while cas>0:
    n=int(input())
    a=[]
    while n>0:
        x=input()
        a=a.__add__([x])
        n=n-1
    for i in range(len(a)):
        find=a[i]
        if find=="porque":
            break
    print(i)
    cas=cas-1
    a=[]