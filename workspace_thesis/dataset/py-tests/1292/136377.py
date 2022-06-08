import sys
for n in sys.stdin:
      l = list(map(int,input().split()))
      s = 0
      for i in l:
            s = s + i
      print(s)