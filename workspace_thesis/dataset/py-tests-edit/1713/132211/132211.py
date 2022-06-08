from sys import stdin

for n in stdin:
    n = int(n)
    s = 0
    for i in range(n):
        x = int(input())
        s = s + x
    print(s)