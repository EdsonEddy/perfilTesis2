n = int(input())
for i in range(n):
    k = int(input()) 
    a = 0
    b = 1
    c = 0
    for j in range(k):
        c = a+b;
        b = a
        a = c
    print(c)
