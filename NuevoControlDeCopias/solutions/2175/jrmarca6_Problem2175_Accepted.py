import sys
n=int(sys.stdin.readline())
for i in range(n):
    x=int(sys.stdin.readline().strip())
    fib1 = 1
    fib2 = 0
    auxf = 0
    for j in range(50):
        auxf = fib2
        fib2 = fib1 + fib2
        fib1 = auxf
        if x==fib1:
            print(j)
            break
