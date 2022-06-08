import sys
from collections import deque
from heapq import *

t = int(input())
for k in range(t):
   cola = deque()
   pq = []
   n, idx = map(int,input().split())
   v = []
   while(len(v)<n):
      v += [int (x) for x in input().split()]
   for i in range(n):
      cola.append((v[i],i))
      heappush(pq,-v[i]) 
   ans = sw = 0
   while(len(pq) and sw==0):
      ans += 1
      a = -heappop(pq)      
      while(len(cola)):
         b = cola.popleft()         
         if(b[0]==a):
            if(b[1]==idx):sw=1
            break
         else:cola.append(b)
   print(ans)
