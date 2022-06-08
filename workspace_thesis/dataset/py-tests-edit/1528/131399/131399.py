c=int(input())
while c>0:
    n =int(input())
    a=n
    c=0
    c1=0
    while n>0:
        d = n % 10
        n = n // 10
        c=c+1
    n=a
    while a>0:
        d1= a % 10
        d2=((a%100)-d)//10
        a = a // 10
        c1=c1+1
        if d1>d2:
            break
    if c1==c:
        print("SI!")
    else:
        print("NO!")
        c=c-1