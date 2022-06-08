s=''
while True:
    n=0
    par=0
    impar=0
    a=input()
    if ( str(a) == s ):
        break
    else:
        a=int(a)
        while (a > 0):
            d=a%10
            a=a//10
            if (n%2 == 0):
                par=par+d
                n=n+1
            else:
                impar=impar+d
                n=n+1
        if (par == impar):
            print ("SI")
        else:
            print ("NO")