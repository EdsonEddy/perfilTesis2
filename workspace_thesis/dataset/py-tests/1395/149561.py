from math import log10
from sys import stdin
for line in stdin:
    s = 0
    n = int(line)
    for i in range(1, n+1):
        s += log10(i)
    print(int(s)+1)