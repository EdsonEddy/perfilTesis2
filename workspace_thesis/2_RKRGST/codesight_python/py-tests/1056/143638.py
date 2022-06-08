n = int(input())
for i in range(n):
    n = int(input())
    cad = input()
    v = list(map(int, cad.split()))
    c = len(v)
    for i in range(c-1, -1, -1 ):
        print(v[i], end=(" "))
    print("")
