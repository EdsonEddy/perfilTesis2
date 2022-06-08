def invertir(x):
    y,inv=x,0
    while y>0:
        d,y=y%10,y//10
        inv=inv*10+d
    if inv==x:
        return 1
while True:
    c=0
    for i in range(int(input())):
        x=int(input())
        if invertir(x)==1:
            c+=1
    print(c)