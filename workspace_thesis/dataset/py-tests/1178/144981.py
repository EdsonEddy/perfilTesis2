import sys
from heapq import *
for x in sys.stdin:
	n = int(x)
	if(n==0):
		break
	B = [int(i) for i in input().split()]
	ans = 0
	A = []
	for i in B:
		heappush(A,i)
	while(len(A)>1):
		a = heappop(A)
		a += heappop(A)
		ans += a
		A.append(a)
	print(ans)
