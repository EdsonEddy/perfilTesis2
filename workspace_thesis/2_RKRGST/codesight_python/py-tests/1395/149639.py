import math

while True:
    n = int(input())
    dig = 0
    for i in range(1,n+1,1):
        if i != 0:
            dig = dig + math.log10(i)
    print(int(dig) + 1)
