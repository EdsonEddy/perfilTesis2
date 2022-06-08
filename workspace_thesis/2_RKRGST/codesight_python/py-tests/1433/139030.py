a,b=map(int,input().split())
i=1
c=0
li=[]
if 1<=a<=1000 and 1<=b<=1000:
    while a<=b:
        for i in range(1,b+1,1):
            if a%i==0:
                c=c+1
            else:
                continue
        if c==2:
            li.append(str(a))
            a=a+1
            c=0
            continue
        else:

            a=a+1
            c=0
            continue
    print(str(len(li)))