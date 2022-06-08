a,b,c=map(int,input().split())
x=a==b
y=b==c
z=a==c
if x==False and y==False and z==False:
    if a>b and a>c:
        print(a)
    if b>c and b>a:
        print(b)
    if c>a and c>b:
        print(c)
if x==True and y==True and z==True:
    print(a)
if x==True and y==False:
    if a > c:
        print(a)
    else:
        print(c)
if y==True and x==False:
    if a > c:
        print(a)
    else:
        print(c)
if z==True and y==False:
    if a > b:
        print(a)
    else:
        print(b)