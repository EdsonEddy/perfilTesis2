import sys
if __name__=='__main__':
   for x in sys.stdin:      
      a, b = map(int,x.split())
      b -= 1
      r = b % a
      s = ( (b//a) + 1 ) % 9
      t = a - r
      u = a - t
      num = str(s)
      if s==0:
         num = '9'
      num = num * t
      res = str(s+1)*u
      print(num+res)