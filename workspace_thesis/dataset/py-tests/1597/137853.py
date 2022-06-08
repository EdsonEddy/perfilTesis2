x = int(input())
for i in range(x):
    a, b =map(str,input().split())
    suma = 0
    sumb = 0
    for k in a:
        suma += int(k)
    for j in b:
        sumb += int(j)
    r = max(suma,sumb)
    print(r)