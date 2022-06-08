n=int(input())
for i in range(n):
    a,b,c=1,0,0
    año=int(input())
    if(año>=1 & año <= 200):
        for l in range(1,año+1):
            c=a+b
            a=b
            b=c
        print(c)
    else:
        break