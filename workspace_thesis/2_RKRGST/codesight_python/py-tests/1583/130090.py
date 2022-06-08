import sys
def MCD(a,b):
   if b==0:
      return a
   return MCD(b,a%b)
def MCM(a,b):
   return a*b//MCD(a,b)
if __name__=='__main__':
    for x in sys.stdin:      
      t = int(x)
      while t:
         t -= 1
         n = int(input())
         v = []
         while len(v)<n:
            v = v+[int(i) for i in input().split()]
         a = 1
         for i in range(n):
            a = MCM(a,v[i])
         print(a)