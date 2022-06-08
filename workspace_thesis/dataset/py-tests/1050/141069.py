while True:
    n=int(input())
    s=""
    s1=""
    b=2;
    while n>0:
        d=n%b
        n=n//b
        s=str(d)+s
    for i in range(len(s)):
        s1=s[i]+s1
    s1=int(s1,2)
    print(s1)