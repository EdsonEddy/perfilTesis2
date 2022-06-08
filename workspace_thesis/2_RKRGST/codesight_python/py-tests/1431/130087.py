import sys
v=[0,1]
for i in range(2,110):
   v.append(v[i-1]+v[i-2])
if __name__=='__main__':
    for x in sys.stdin:      
      n, m, a, b = map(int,x.split())
      v = [a%m,b%m]
      for i in range(2,n):
         v.append((v[i-1]%m + v[i-2]%m)%m)
      print(v[n-1])