n=int(input())

while n!=0:
    n=n-1
    x=int(input())
    y=0
    while x>0:
        d=x%10
        x=int(x/10)
        
       
        esprimo=True
        for i in range(2,int(d/2)+1):
            if d%i==0 or  d == 1:
                esprimo=False
        if esprimo == True and d!=0 and d!=1:
            y=y*10+d
    print(int(str(y)[::-1]))
