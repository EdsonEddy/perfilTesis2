from sys import stdin

for i in stdin:
    n = int(i)
    if n == -1:
        break
    if 0 <= n <= 1000:
        s = 1
        for j in range(0, n):
            s = s + 2
        print(s)