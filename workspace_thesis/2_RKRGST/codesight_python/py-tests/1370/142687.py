while True:
    x=int(input())
    s=''
    b=2;
    while x>0:
        d=x%b
        x=x//b
        s=str(d)+s
    print(len(s))
