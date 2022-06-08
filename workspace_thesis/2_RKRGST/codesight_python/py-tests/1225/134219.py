a,b,c=map(int,input().split())
x=a==b
y=b==c
z=a==c
if x==False and y==False and z==False:
    if a>b and a>c:
        print(a)
    if b>a and b>c:
        print(b)
    if c>a and c>b:
        print(c)
if x==True and y==False and z==False:
    if b>c:
        print(b)
    else:
        print(c)
if y==True and x==False and z==False:
    if b>a:
        print(b)
    else:
        print(a)
if z==True and x==False and y==False:
    if b>a:
        print(b)
    else:
        print(a)
if z==True and x==True and y==True:
    print(a)
