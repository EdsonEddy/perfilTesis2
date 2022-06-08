import sys

for linea in sys.stdin:
  v = [int(x) for x in linea.split()]
  del v[0]
  print(max(v))