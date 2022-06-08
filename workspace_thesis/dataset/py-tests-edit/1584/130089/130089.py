import sys
v=[0,1]
for i in range(2,110):
   v.append(v[i-1]+v[i-2])
if __name__=='__main__':
    for x in sys.stdin:      
      n = int(x)
      v = []
      while len(v)<n:
         v = v+[int (i) for i in input().split()]
      v.sort()
      print(v[n-1]-v[0])