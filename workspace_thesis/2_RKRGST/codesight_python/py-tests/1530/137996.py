def isprime(k):
    if(k == 2 or k == 3 or k == 5 or k == 7):
        return True
    else:
        return False

import math
n = int(input())
for i in range(n):
    x = int(input())
    res = 0
    po = int(math.log10(x))
    while(x != 0):
        dig = x // pow(10, po)
        x = x % pow(10, po)
        po-=1
        flag = isprime(dig)
        if(flag == True):
            res = res*10 + dig
    print(res)
