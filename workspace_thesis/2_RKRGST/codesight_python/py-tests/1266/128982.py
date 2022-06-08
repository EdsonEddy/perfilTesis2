from sys import stdin
for i in stdin:
	d,x=map(int,i.split())
	a=input().split()
	e=d-1
	s=int(a[0])
	s=s*(x**e)
	for j in range(1,d,1):
		aa=int(a[j])
		e-=1
		s=s+aa*(x**e)
		
	print(float(s))
	