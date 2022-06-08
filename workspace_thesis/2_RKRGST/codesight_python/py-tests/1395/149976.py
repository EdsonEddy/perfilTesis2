import math
while True:
    n=int(input())
    c=0
    for i in range (1,n+1):
        c=c+math.log10(i)
    print(int(c+1))
    