while True:   
    cas=int(input())
    c1=0
    while cas>0:
        a=input()
        pal=a[::-1]
        if pal==a:
            c1=c1+1
        cas=cas-1
    print(c1)