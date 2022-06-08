import sys
v = [0,1]
for i in range(2,201):
   v.append(v[i-1]+v[i-2])
if __name__=='__main__':
    for x in sys.stdin:      
      n = int(x)
      while n:
         n -= 1
         i = int(input())
         print(v[i])
