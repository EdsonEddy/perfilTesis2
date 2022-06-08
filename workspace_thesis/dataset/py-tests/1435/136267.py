import math
n, k = map(int,input().split())
l = int( math.log10(n)+1 )
k = l-k
c = 0
p = -1
while( n>0 ):
   if(c==k):
      p = n%10
   n = n//10
   c += 1
print(l,p)
