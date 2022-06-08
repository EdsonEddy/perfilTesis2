import sys
def isPrime(n):
    if(n<2):
        return 0
    d=2
    while(d*d<=n):
        if(n%d==0):
            return 0
        d=d+1
    return 1

for x in sys.stdin:
    n=int(x)
    if(isPrime(n)):
        print ("ES PRIMO")
    else:
        print ("NO ES PRIMO")
