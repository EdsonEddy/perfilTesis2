x = (input())
lar = len(x)
if lar % 2 != 0:
    lon = lar // 2
    print(x[lon])
else:
    print('*')