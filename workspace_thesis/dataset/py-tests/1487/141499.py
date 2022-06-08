import sys
def isprime(n):
    if(n<2):
        return 0
    i=2
    while(i*i<=n):
        if(n%i==0):
            return 0
        i=i+1
    return 1
for x in sys.stdin:
    n=int(x)
    if (isprime(n)):
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")