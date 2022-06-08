def primo(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c=c+1
    if c==2:
        r=1
    else:
        r=0
    return r
t=int(input())
for q in range(t):
    n=int(input())
    y=n
    x=0
    p=1
    while y>0:
        d=y%10
        y=y//10
        if primo(d)==1:
            x=d*p+x
            p=10*p
    if x==0:
        print(-1)
    else:
        print(x)