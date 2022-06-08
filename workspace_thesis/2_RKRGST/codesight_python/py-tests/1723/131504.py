while 2>0:
    from math import log10
    a,b=map(int,input().split())
    diga=log10(a)+1
    diga1=int(diga)
    digb=log10(b)+1
    digb1=int(digb)
    c=0
    while a !=0 and b!=0:
        dig1 = a % 10
        a=a//10
        dig2 =b%10
        b=b//10
        if dig1!=dig2:
            c=c+1
        if c==2:
            print("lentes")
            break
    if c !=2:
        print("feliz")