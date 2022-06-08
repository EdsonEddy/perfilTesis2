while 1>0:
    w=int(input())
    x=0
    for z in range (1,w+1):
        a=input()
        def f(x):
            return x[::-1]
        if a == f(a):
            x = x + 1
    print(x)