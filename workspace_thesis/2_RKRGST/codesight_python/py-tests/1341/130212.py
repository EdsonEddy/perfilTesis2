from math import sqrt 

def fib(n):
    if n < 2:
        return n
    else:
        u = ((1+sqrt(5))/2)
        j = ((u**n-(1-u)**n)/sqrt(5))
        return round(j)
while True:
    m=int(input())
    if(m<100):
        y=fib(m)
        print(y)