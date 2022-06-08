import math
y=1
while y!=0:
    n=int(input())
    if n==0:
        y=0
    t=int(math.log10(n+1))
    nn=n
    aux=0
    u=["","i","ii","iii","iv","v","vii","vii","viii","ix"]
    d=["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"]
    c=["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    m=["","m","mm","mmm"]
    un=int(nn%10)
    de=int(nn/10)%10
    ce=int(nn/100)%10
    mi=int(nn/1000)%10
    if(n!=0):
        if(n>=1000):
            print(str(n)+" => "+str(m[mi])+str(c[ce])+str(d[de])+str(u[un]))
        elif(n>=100):
            print(str(n)+" => "+str(c[ce])+str(d[de])+str(u[un]))
        elif n>=10:
            print(str(n)+" => "+str(d[de])+str(u[un]))
        elif n<=9:
            print(str(n)+" => "+str(u[un]))