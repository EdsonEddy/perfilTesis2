n=int(input())
for i in range(n):
    piedras, palitos = map(int, input().split())
    p1 = int(piedras / 3)
    p2 = int(palitos / 2)
    r = piedras % 3 + palitos % 2
    if p1 < p2:
        r = 2 * (p2 - p1) + r
        print(p1, r)
    elif p1 == p2:
        print(p1, r)
    else:
        r = 3 * (p1 - p2) + r
        print(p2, r)
