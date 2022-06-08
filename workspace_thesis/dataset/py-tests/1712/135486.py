import sys
for i in sys.stdin:
   if i=='fin':
      break
   n = int(i)
   suma = 0
   for j in range(n):
      a = int(input())
      suma += a
   print(suma)
