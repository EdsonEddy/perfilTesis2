
a, b, c = map( int, input().split())
if a==b==c:
    print(a)
else:
    if a==b or b==c or a==c:
        if a==b:
            if b>c:
                print(b)
            else:
                print(c)
        if b==c:
            if c>a:
                print(c)
            else:
                print(a)
        if a==c:
            if c>b:
                print(c)
            else:
                print(b)
    else:
        if a>b:
            if a>c:
                print(a)
            else:
                print(c)
        if b>c:
            if b>a:
                print(b)
        if c>a:
            if c>b:
                print(c)
            else:
                print(b)