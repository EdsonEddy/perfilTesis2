for _ in range(int(input())):
    n=int(input())
    fibo=[0]
    x=1
    y=0
    for i in range(100):
        if n in fibo:
            print(len(fibo)-1)
            break
        f=x+y
        fibo.append(f)
        x=y
        y=f
