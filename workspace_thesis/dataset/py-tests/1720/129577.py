import sys
if __name__=='__main__':
    for x in sys.stdin:
      t = int(x)
      x = y = z = 0
      while t:
         t -= 1                
         a, b, c = map(int,input().split())
         x += a
         y += b
         z += c
      if not x and not y and not z :print('YES')
      else: print('NO')



   