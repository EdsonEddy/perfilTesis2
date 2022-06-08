import math
import sys
def isprime(n):
    if n < 2:
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if ( n % i == 0):
            return False
    return True


for k in sys.stdin:
    k = int(k)
    if(isprime(k)):
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")


