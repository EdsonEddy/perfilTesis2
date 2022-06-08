x=True
while x==True:
    z=int(input())
    if z==0:
        x=False
    else:
         n=tuple(input().split())
         s=len(n)
         r=0
         for i in range(0,s,1):
              r=r+int(n[i])
         print(r)