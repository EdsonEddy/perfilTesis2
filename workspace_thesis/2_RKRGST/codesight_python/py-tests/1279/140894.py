from sys import stdin
for sd in stdin:
    abc="abcdefghijklmnopqrstuvwxyz"
    a,b=map(str,sd.split())
    s=''

    a=int(a)
    while a>26:
        a=a-26
    for i in b:
        if i=="_":
            s=s+" "
        elif i in abc:
            d=abc.find(i)
            f=d+a
            if f<26:
                s=s+abc[f]
            else:
                s=s+abc[f-26]
        else:
            s=s+i

    s=s.upper()
    print(s)