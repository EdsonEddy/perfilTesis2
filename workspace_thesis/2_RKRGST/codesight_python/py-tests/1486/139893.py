def fib(n):
    i=1
    j=1
    for l in range(n):
        k=j
        j=i+j
        i=k
    return i

x = int(input())
for i in range(1,x+1):
    if i%2!=0:
        print(fib(int(i/2)))
    else:
        print(i)