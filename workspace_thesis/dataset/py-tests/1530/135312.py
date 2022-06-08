import math

T  = int(input())
for i in range(T):
    n = int(input())
    dig = int(math.log10(n))
    m = 0
    for i in range(dig+1):
        d = int(n/math.pow(10,dig-i))
        n = int(n%math.pow(10,dig-i))
        if d==2 or d==3 or d==5 or d==7:
            m = m*10 + d
        else:
            pass
    if m==0:
        print('0')
    else:
        print(m)