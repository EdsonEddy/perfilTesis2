from sys import stdin
for sd in stdin:
    a,b=map(str,sd.split())
    a=int(a)
    s=''
    while a>26:
        a=a-26
    abc='abcdefghijklmnopqrstuvwxyz'
    for  i in b:
        if i in abc:
            d=abc.find(i)
            c=d+a
            if c>=26:
                c=c-26

                s=s+abc[c]
            else:
                s=s+abc[c]
        elif i=='_':
            s=s+' '
        else:
            s=s+i
    print(s.upper())