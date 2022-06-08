while True:
    a=int(input())
    r=0
    i=0
    b=0
    c=0
    while a>0:
        d=a%10
        r=r*10+d
        a=a//10
        i=i+1
        if i%2==0:
            b=b+d
        else:
            c=c+d
    if b==c:
        print("SI")
    else:
        print("NO")
