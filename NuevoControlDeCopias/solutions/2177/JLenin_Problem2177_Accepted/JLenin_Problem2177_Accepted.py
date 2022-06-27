for _ in range(int(input())):
    n,k=map(int,input().split())
    x=''
    while n>0:
        m=n%10**k
        c=0
        p=m
        if m!=0:
            while m>0:
                i=m%10
                m//=10
                c+=1
            if c==k:
                while True:
                    s=0
                    for j in str(p):
                        s+=int(j)
                    if s<10:x=str(s)+x;break
                    else:p=s
        else: x=str(m)+x
        n//=10
    print(x)
