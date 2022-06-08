from sys import stdin
#for line in stdin:
for line in stdin:
   a, b = map(int, line.split())
   if 1 <= b <= a <= 10**12:
      na = a//2 if a % 2 == 0 else a // 2 + 1
      if b < a/2:
         print(2*b-1)
      else:
         print((b - na)*2)