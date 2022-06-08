import sys
if __name__=='__main__':
   for x in sys.stdin:
      n, suma = map(int,x.split())
      j = n-1
      i = 0
      sw = 1
      v = []
      while len(v)<n:
         v = v+[int (i) for i in input().split()]
      v.sort()
      while i<j and sw:
         if v[i]+v[j]==suma:
            sw = 0
         elif v[i]+v[j]>suma:
            j -= 1
         else: i += 1
      if sw:print(-1)
      else: print(v[i],v[j])