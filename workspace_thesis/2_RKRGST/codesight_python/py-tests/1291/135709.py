import sys
v = []
for i in sys.stdin:
   v += [int(x) for x in i.split()]
   if(v[-1]==0):
      print(sum(v))
      v=[]
