import sys
import math
def primo(x):
    if(x < 2):
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True

for n in sys.stdin:
    n = int(n)
    if(primo(n) == True):
        print("ES PRIMO")
    else:
        print("NO ES PRIMO")