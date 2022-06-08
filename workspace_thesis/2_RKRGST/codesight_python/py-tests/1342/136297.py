t=int(input())
for i in range(t):
	n,m=map(int,input().split())
	a,b,c=-1,1,0
	for j in range(n+1):
		c=(a%m+b%m)%m
		a=b
		b=c
	print(c)