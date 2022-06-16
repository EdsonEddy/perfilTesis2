x=int(input())
for i in range(x):
    n=int(input())
    a=0
    b=1
    cont=0
    while n!=a:
        f=a+b
        a=b
        b=f
        #print(f)
        cont=cont+1
    print(cont)
