import math
from sys import stdin, stdout
for z in stdin:
    n = int(z)
    dig = 0
    for i in range(1,n+1,1):
        if i != 0:
            dig = dig + math.log10(i)
    stdout.write(str(int(dig) + 1) + "\n")
