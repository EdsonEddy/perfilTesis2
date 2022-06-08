x=int(input())
if x>=1 and x<=10000:
    if x%3==0:
        if x==6 or x==3:
            if x==6:
                print(3)
            else:
                print(0)
        else:    
            n1=x-3
            n2=n1-3
            n3=n2-3
            print(n1+n2+n3)
    else:
        if x==5 or x==1 or x==2:
            if x==5:
                print(3)
            else:
                print(0)
        else: 
            r=x%3
            n1=x-r
            n2=n1-3
            n3=n2-3
            print(n1+n2+n3)