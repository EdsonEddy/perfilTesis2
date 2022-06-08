n=int(input())
a1=0
for i in range(n):
    a,b=map(int,input().split(" "))
    if a>b:
        while a1<=a:
            a1=a1+1
            if a%a1==0 and b%a1==0:
                mcd=a1
    else:
        while a1<b:
            a1=a1+1
            if a%a1==0 and b%a1==0:
                mcd=a1
    a1=0
    print(mcd)