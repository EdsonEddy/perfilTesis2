casos=int(input())
for i in range (casos):
    n=int(input())
    a=-1
    b=1
    fibo=7778742049
    cont=0
    while (n>0):
        cont=cont+1
        fibo=a+b
        a=b
        b=fibo    
        if (n==fibo):             
            break 
    if(n==0):
        print(0)
    else:
        print(cont-1)    
