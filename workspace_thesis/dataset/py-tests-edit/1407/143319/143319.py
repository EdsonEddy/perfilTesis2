t = int(input())
for j in range(t):
	n = int(input())
	v = []
	while(len(v)<n):
		v += [int(x) for x in input().split()]
	ans = 0
	for i in range(1,n-1):
		if(v[i]>v[i-1] and v[i]>v[i+1]):
			ans += 1
	print(ans)