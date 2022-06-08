a,b,c=map(int,input().split())
c=c+1
if c//60!=0:
    c=0
    b=b+1
if b//60!=0:
    b=0
    a=a+1
if a//24!=0:
    a=0
print("{:02d}:{:02d}:{:02d}".format(a,b,c))