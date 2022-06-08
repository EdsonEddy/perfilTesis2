a,b=map(int,input().split())
if a>b:
    mayor=a
    menor=b
if b>a:
    mayor=b
    menor=a
if a==b:
    print(a)
for i in range(mayor,menor-1,-1):
    print(i)
