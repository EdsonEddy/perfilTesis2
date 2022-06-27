t=int(input())
for k in range(t):
    x,y=map(int,input().split())
    #x,y=3728954, 2
    #x,y=3728954, 3
    a=x
    cont=0
    dig=0
    b=0
    nuevo_x=0
    d=1
    while a>0:
        cont1=1
        a=x//10**cont
        c=a%10
        #print(a,c)
        while cont1<y:
            a=a//10
            b=a%10
            dig=c+b
            #print(a,b,c,dig)
            c=dig
            cont1=cont1+1
        if dig>9:
            while dig>9:
                e=dig%10
                d=dig//10
                dig=e+d
                #print(e, d, dig)
        nuevo_x=nuevo_x+dig*10**cont
        #print (dig, cont, nuevo_x)
        cont=cont+1
    nx=nuevo_x%(10**(cont-1))
    if nx>0: print(nx)
    else: print('')
