def inv(c):
    s = ''
    for i in range(len(c) - 1, -1, -1):
        s = s + c[i]
    return s


n = int(input())
a = []
for x in range(n):
    c = input()
    a.append(inv(c))
for j in range(len(a) - 1, -1, -1):
    print(a[j])