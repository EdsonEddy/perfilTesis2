n=int(input())
for i in range(0,n,1):
	r,p=map(int,input().split())
	p1=p//2
	r1=r//3
	if p1>0 and r1>0:
		s=min(r1,p1)
		b=p-2*s+r-3*s
		print(s,b)
	else:
		b=r+p
		print(0,b)
		