import sys

v = []
for n in sys.stdin:
  n = int(n)
  for i in range(n):
      m,a,b = map(int,input().split())
      v = list(map(int,input().split()))
               
      acu = [0 for i in range(len(v) + 1)]
      for j in range(1, len(acu)):
          acu[j] = acu[j-1] + v[j-1]
               
      print(acu[b+1] - acu[a])