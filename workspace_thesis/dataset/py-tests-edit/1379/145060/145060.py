from sys import stdin

for x in stdin:
    m = int(x)
    if m == 0:
        break
    a = input().split()
    a.sort()
    for i in range(len(a) - 1, -1, -1):
        print(a[i], end='')
    print()