import math
n = int(input())
for i in range(n):
    x = int(input())
    aux = x
    su = 0
    while(aux!=0):
        su = su + (math.factorial(aux % 10))
        aux = aux // 10
    
    if(x == su):
        print("Y")
    else:
        print("N")