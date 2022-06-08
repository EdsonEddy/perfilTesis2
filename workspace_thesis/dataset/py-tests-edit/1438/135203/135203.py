import math
n, i, j = map(int,input().split())
aux = n
if(i>j):
    ss=i
    i = j
    j = ss
l = int( math.log10(n) + 1)
i = l - i
j = l - j
di = (n%10**(i+1)) // 10**i
dj = (n%10**(j+1)) // 10**j
num = (n // 10**(i+1) ) * (10**(i+1))
num += (dj*10**i)
n %= 10**i
num += ( n//(10**(j+1)) ) * 10**(j+1)
num += di * 10**j
n %= 10**j
num += n
if(l==1):
    print(aux)
else:
    print(num)
