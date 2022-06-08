def serie(s):
    s=s%6
    r=2**(s+1)
    x=0
    y=str(r)
    con=True
    while con==True:
        for a in y:
            x=x+int(a)
        if x<10:
            con=False
        else:
            y=str(x)
            x=0
    return(x)

while True:
    n=int(input())
    for i in range(n):
        s=int(input())
        print(serie(s))