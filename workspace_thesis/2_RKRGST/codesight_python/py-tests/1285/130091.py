import sys
def MCD(a,b):
   if b==0:
      return a
   return MCD(b,a%b)
def MCM(a,b):
   return a*b//MCD(a,b)
if __name__=='__main__':
    for x in sys.stdin:      
      n = int(x)
      a = b = 0;
      sw = True
      while n:
         if sw: a+=n%10
         else:  b+=n%10
         n = n//10
         sw = not sw
      if a==b:print('SI')
      else: print('NO')
