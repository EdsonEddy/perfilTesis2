t = int(input())
for i in range(t):
	x, y = map(int,input().split())
	a = b = c = -1
	a = x ^ y
	if((y|x)==y):b = x ^ y
	if((y|x)==x):c = x & y
	print(a,b,c)

