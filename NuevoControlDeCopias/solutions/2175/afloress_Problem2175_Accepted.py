#2175 Problem C Otra vez Fibonacci
casos=int(input())
for i in range(1,casos+1):
    n=int(input())
    cont=0
    a=-1
    b=1
    while True:
        x=a+b
        
        a=b
        b=x
        cont=cont+1
        if n==x:
            print(cont-1)
            break
            

