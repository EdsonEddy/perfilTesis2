# 1486 - modular2
# Jhonny

n = int(input())
par = 2
a = 1
b = 0
for i in range(1, n+1):
    if i % 2 == 1:
        c = a + b
        a, b = b, c
        print(c)        
    else:
        print(par)
        par = par + 2
        
