a,b,c=map(int,input().split())
x=a==b
y=b==c
z=a==c
if x==False and y==False and z==False:
    if a>b and a>c:
        if b>c:
            print(c,b,a)
        else:
            print(b,c,a)
    if c > b and c > a:
        if b > a:
            print(a, b, c)
        else:
            print(b, a, c)
    if b > a and b > c:
        if a > c:
            print(c,a, b)
        else:
            print(a, c, b)
if x==True and y==True and z==True:
    print(a,b,c)
if x==True and y==False:
    if a > c:
        print(c, b, a)
    else:
        print(b, a, c)
if y==True and x==False:
    if a > c:
        print(c, b, a)
    else:
        print(a, b, c)
if z==True and y==False:
    if a > b:
        print(b, c, a)
    else:
        print(c, a, b)
