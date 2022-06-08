t = int(input())
for i in range(t):
	n, m = map(int,input().split())
	ans = 0
	v = []
	while(len(v)<m):
		v += [int (x) for x in input().split()]
	for mask in range(1,1<<m):
		a = 1
		s = 0
		for i in range(m):
			if(mask&(1<<i)):
				s += 1
				a *= v[i]
		#print('ans=',ans)
		if( s&1 ):ans += n//a
		else:     ans -= n//a
	print(ans)
