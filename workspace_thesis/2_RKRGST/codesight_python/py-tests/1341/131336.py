from sys import stdin
for n in stdin:
    i = int(n)
    if 0 < i <= 100:
        a = 0
        b = 1
        while i > 1:
             a, b = b, a + b
             i -= 1
        print(b)
    else:
        print(0)