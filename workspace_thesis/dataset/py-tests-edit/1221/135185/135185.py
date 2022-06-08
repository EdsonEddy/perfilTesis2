a,b,c=map(int,input().split())
if(a<b and a<c):
    if b>c:
        print(a,c,b)
    else:
        print(a,b,c)
elif b>a and b>c:
    if a>c:
        print(c,a,b)
    else:
        print(a,c,b)
else:
    if b<c and b<a:
        if a<c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        if c<b and c<a:
            if b<a:
                print(c,b,a)
            else:
                print(c,a,b)
