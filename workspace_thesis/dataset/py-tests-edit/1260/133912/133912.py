x=int(input())
for i in range(x):
    n1,n2=map(int,input().split())
    a=max(n1,n2)
    b=min(n1,n2)
    if a>=2 and a<=10**5 and b>=2 and b<=10**5:
        while b!=0:
            res=b
            b=a%b
            a=res
        print(res)
      