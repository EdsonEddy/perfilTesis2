def fib(n):
    i=0
    j=1
    for l in range(n):
        k = j
        j = i+j
        i = k
    return k

n = int(input())
cont = 0
for i in range(n):
    cont = cont+1
    if cont%2!=0:
        print(fib(int(cont/2+1)))
    else:
        print(cont)