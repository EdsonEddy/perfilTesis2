while True:
    n = input()
    if n != 0:
        L = list(map(int,input().split()))
        s = sum(L)
        print(s)
