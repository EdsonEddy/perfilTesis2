A = int(input())
for i in range(1, A+1):
    x = int(input())
    a = 1
    b = 0
    s = 0
    for j in range(1, x+1):
        c = a+b
        a = b
        b = c
    print(c)
print()