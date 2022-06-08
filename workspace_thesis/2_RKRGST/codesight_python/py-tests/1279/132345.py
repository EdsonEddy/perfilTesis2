from sys import stdin
for df in stdin:
    a,b=map(str,df.split())
    a=int(a)
    s=''
    while a>26:
        a=a%26

    abc='abcdefghijklmnopqrstuvwxyz'
    for i in b:
        if i in abc:
            d=abc.find(i)
            cx=d+a
            if cx>=26:
                k=26-a
                cx=d-k
            j=abc[cx]
            s=s+j
        elif i=='_':
            s=s+' '
        else:
            s=s+i
    print(s.upper())