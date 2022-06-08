n = int(input())
a = 1
b = 0
p = 0
sw = 0
while n > 0:
    
    if sw == 0:
        f = a + b
        a = b
        b = f
        print(f)
        sw = 1
        n = n - 1
    else:
        p = p + 2
        print(p)
        sw = 0
        n = n - 1