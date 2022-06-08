import sys
N = 10**5 + 1
v = [0] * N
i = 2
while i<N:
   v[i] += 1
   i += 2
i = 3
while i<N:
   if v[i]==0:
      j = i;
      while j<N:
         v[j] += 1
         j += i
   i += 2
if __name__=='__main__':
   for x in sys.stdin:
      a, b = map(int,x.split())
      mx = div = 0
      while a<=b:
         if v[a]>=div:
            div = v[a]
            mx = a
         a += 1
      print(f'{mx} tiene {div} divisores')