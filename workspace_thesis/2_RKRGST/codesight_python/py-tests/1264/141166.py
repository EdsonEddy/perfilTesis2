n=int(input())
c1=1
while c1<=n:
    f,c=map(int,input().split())
    s=0
    sw=1
    for i in range (f):
        x=input().split()
        if i%2!=0:
            sw=0
        else:
            sw=1
        for j in x:
            d=int(j)
            if sw==1:
                s=s+d
                sw=0
            else:
                sw=1
    print(s)