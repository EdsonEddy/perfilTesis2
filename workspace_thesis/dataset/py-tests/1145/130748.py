n=int(input())
for j in range(1,n+1):
    a=int(input())
    if(a>=1 and a<=200):
        c = 1
        d = 1
        for i in range(3,a+1):
            c,d=d,c+d
        print(d)
    else:
        exit()