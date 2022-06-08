import math
n,k=map(int,input().split())
if 1 <= n and n <= 1*(10**18):
    d = int(math.log10(n))+1
    if k <= d:
          c=d-k
          f=1*(10**c)
          p=n//(1*(10**c))
          p=p%10
          print(d,p)