import math
while True:
    n=int(input())
    if n>1:
        c=1
        i=2
        while i<=int(math.sqrt(n)):
            if n%i==0:
                c=0
            i=i+1
        if c==1:
            print("ES PRIMO")
        else:
            print("NO ES PRIMO")
