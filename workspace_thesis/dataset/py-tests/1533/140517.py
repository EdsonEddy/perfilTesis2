from sys import *
for line in stdin:
      n,k=map(int,line.split())
      if 1<=k and k<=n and n<=10**12:
            if n%2==0:
                  t=n//2
            else:
                  t=n//2+1
            if k>t:
                  r=(k-t)*2
            else:
                  r=(k*2)-1
      print(r)