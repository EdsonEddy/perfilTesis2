import sys
for l in sys.stdin:
   if int(l)==0:
       break
   i=0
   a = list(map(int,input().split()))
   print(sum(a))