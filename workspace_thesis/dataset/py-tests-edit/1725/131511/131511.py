from sys import stdin
for line in stdin:
    k, t = map(int, line.split())
    if 80 <= k <= 160 and 80 <= t <= 163800:
        i = 0
        while t > 0:
            t -= (k*(2**i))
            i += 1
        print(i)