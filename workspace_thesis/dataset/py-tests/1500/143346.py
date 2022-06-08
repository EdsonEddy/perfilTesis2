n = int(input())
a = [int(x) for x in input().split()]
ln = [] * n
for i in range(n - 1, -1, -1):
    ln.append(a[i])
if a == ln:
    print('SI')
else:
    print('NO')