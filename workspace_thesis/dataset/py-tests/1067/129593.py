import sys
if __name__=='__main__':
    for x in sys.stdin:
      t = int(x)
      while t:
         t -= 1
         n = int(input())
         v = []
         ans = 0
         while len(v)<n:
            v = v+[ int (i) for i in input().split()]
         for i in range(len(v)):
            if not(i&1):
               ans ^= v[i]
         if n&1:print(ans)
         else: print(0)
         



