n=int(input()) #primer dato
while n<1 or n>10000:
    n=int(input())
for i in range(n): #n veces
    y=[]
    s=0
    nn=int(input()) #numero de datos
    while nn<0 or nn>1000:
        nn=int(input())
    y=input().split() # entra de datos
    for j in range(0,nn): # evalua dato por dato
        ########## para saber si es primo o no
        def multiple(valor):
            resto = valor % 3
            if resto == 0:
                return True
            else:
                return False
        ###########
        v=int(y[j])  #castea el valor a un numero
        ss=v*2
        multiple = multiple(v*2)
        if multiple == True: #lo suma si es primo
            s=s+ss

    print('La suma es',s)
