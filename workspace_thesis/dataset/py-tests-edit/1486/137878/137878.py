def fibo(n):
    a = 1
    b = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
    return c
se2 = 0
cf = 1
x = int(input())
for i in range(1,x+1):
    if i % 2 == 0:
        se2 += 2
        print(se2)
    else:
        print(fibo(cf))
        cf+=1