while True:
    a,b=map(str,input().split())
    a=int(a)
    a=a%26
    aM="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    am="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    x=""
    for d in b:
        if d=="_":
           d=" "
        elif d in am:
           e=am.find(d)
           f=e+a
           g=aM[f]
           d=g
        x=x+d
    print(x)