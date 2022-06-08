t=int(input())
for j in range(t):
	n,a,b=map(int,input().split())
	v=input().split()
	ans=0
	for i in range(len(v)):
		if i>=a and i<=b:
			ans+=int(v[i])
	print(ans)