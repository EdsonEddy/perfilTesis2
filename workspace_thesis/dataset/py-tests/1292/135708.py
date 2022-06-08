import sys
for i in sys.stdin:
   n = int(i)
   if(n==0):break
   v=[]
   while(len(v)<n):
      v += [int(x) for x in input().split()]
   print(sum(v))
