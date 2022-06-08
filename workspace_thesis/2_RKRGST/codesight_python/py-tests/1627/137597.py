n=int(input())
for j in range(n):
	s=0
	k,n=map(int,input().split())
	if k%2==0:
		m=k//2
		r=(k*n+n)*m
	else:
		m=(k+1)//2
		r=k*n*m
	print(r)