a,b,c=input().split()
may=int(a)
for i in range(3):
    if int(a)>may:
        may=int(a);
    a=b
    b=c
print(may)