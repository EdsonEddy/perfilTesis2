n = int(input())
c = 0
for _ in range (n):
    x = int(input())
    cad = input().split()
    c = 0
    for i in cad:
        if int(i) % 3 == 0:
            m = 2 * int(i)
            c = c + m
    print("La suma es",c )
