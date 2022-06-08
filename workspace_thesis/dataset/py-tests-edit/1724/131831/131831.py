import sys
for x in sys.stdin:
	n, k = map(int, x.split())
	if (k*(k+1)//2)<=n:
		print('posible')
	else:
		print('imposible')