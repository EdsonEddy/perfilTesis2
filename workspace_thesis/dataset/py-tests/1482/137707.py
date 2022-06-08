while True:
    x = int(input())
    n = -1
    for i in range(1,x+1):
        n = (i * n)
        if i % 2 == 0:
            print(n*-1)
        else:
            print(n)