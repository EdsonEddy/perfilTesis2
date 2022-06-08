def find(padre,u):
	if(padre[u]!=u):
		padre[u] = find(padre,padre[u])
	return padre[u]

t = int(input())
while(t):
	# n = m = 0
	try:
		n,m= map(int,input().split())    	
	except ValueError:
		continue
	t -= 1
	P = []
	for i in range(n+1):
		P.append(i)
	for i in range(m):		
		x, y = map(int,input().split())
		x = find(P,x)
		y = find(P,y)
		if(x!=y):
			P[x] = y	
	x, y = map(int,input().split())
	x = find(P,x)
	y = find(P,y)
	if(x==y):print('SI')
	else:print('NO')