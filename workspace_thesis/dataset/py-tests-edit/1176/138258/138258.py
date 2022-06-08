import sys
from heapq import *

for k in sys.stdin:
   N, lim, ini = map(int,k.split())
   heap = []
   
   for i in range(N):
      x,y = map(str, input().split())
      heappush(heap,int(x))
   
   ans = ini+heappop(heap);
   if(ans<=lim):print(ans)
   else:print('Mil disculpas, regrese mañana')   
   while (len(heap)):      
      heap.pop()
      ans += ini
      if(ans<=lim):print(ans)
      else:print('Mil disculpas, regrese mañana')
