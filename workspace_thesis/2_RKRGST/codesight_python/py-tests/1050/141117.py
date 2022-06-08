from math import  log
x=int(input())
y=0
while x!=0:
    while x>0:
        d=x%2
        x=x//2
        y=y*10+d
    a=int(log(y*10))+1
    t=0
    for i in range (a):
        d=y%10
        y=y//10
        t=d*(2**i)+t
    print(t)
    x=int(input())
