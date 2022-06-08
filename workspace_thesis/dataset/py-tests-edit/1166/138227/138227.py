import sys
s = set()
n = x = y = 0
def fun(a, b):
   if(a>n or b>10):
      return
   s.add(a)
   fun(10*a + x, b+1)
   fun(10*a + y, b+1)
for i in sys.stdin:
   n = int(i)
   s.clear()
   for x in range(10):
      for y in range(x+1,10):
         fun(0,0)
   print(len(s)-1)
