x=int(input())
for i in range(x):
	c=int(input())
	v = list(map(int,input().split()))
	p=0
	for u in range(1,c):
		if v[u-1]<v[u]>v[u+1]:
			p+=1
	print(p)