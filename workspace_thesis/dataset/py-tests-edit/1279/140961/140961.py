while True:
    a,b=map(str,input().split())
    a=int(a)
    a=a%26
    h="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    x=""
    for d in b:
       if d=="_":
           d=" "
       elif d in c:
             e=c.find(d)
             f=e+a
             g=h[f]
             d=g
       x=x+d
    print(x)