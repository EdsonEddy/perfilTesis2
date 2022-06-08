n = int(input())
a = 0
b = 1
x = 2
for i in range (n):
    if i % 2 == 0:
        f = a + b
        a = b
        b = f
        print(a)
    else:
        print(x) 
        x = x+2