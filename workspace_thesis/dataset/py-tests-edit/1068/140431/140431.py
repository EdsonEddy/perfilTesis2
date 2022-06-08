cu = int(input())
for y in range(cu):
    n = int(input())
    cad = list()
    for x in range(n):
        pa = input()
        cad.append(pa.lower())
    tot = cad.index("porque")
    print(tot)
