while True:
    n=input()
    b=n[1:len(n):2]
    c=n[0:len(n):2]
    b=int(b)
    c=int(c)
    s1=0
    while c>0:
        d=c%10
        c=c//10
        s1=d+s1
    s2=0
    while b>0:
        j=b%10
        b=b//10
        s2=j+s2
    if s1==s2:
        print("SI")
    else:
        print("NO")