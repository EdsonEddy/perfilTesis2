import math
n = int(input())
while n > 0:
    x = int(input())
    aux = x
    p = 0
    while x > 0 :
        r = (x // 10) *10
        dig = x - r
        
        x = x // 10
        
        c = math.factorial(dig)
        
        p = p + c
    if p == aux:
        print("Y")
    else:
        print("N")
    n = n - 1
