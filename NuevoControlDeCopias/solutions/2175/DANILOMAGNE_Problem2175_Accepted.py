for _ in range(int(input())):
    n=int(input())
    fib = [0]
    a,b=1,0
    for i in range (100):
        if n in fib:
            print(len(fib)-1)
            break
        f = a + b
        fib.append(f)
        a=b
        b=f
