from sys import *
for casos in stdin :
    K,T=map(int,casos.split())
    T //= K
    ans = 0
    while T > 0:
      T //= 2
      ans += 1
    print(ans)