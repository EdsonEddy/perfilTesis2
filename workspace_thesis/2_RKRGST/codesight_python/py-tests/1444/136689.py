z=int(input())
for asg in range (1,z+1):
    a=int(input())
    b=bin(a)
    c,b=b.split("b")
    x=0
    y=0
    for d in b:
        if d=="1":
            x=x+1
        elif d=="0":
            x=x*0
        if(x==2):
            y=y+1
            x=x*0
    print(y)
