import math
while True:
    n=int(input())
    s=0
    for i in range (1,n+1,+1):
        s=s+ math.log10(i)
    cd=int(s+1)
    print(cd)