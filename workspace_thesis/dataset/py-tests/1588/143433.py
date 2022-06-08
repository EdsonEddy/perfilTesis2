n=int(input())
for i in range (n):
	x=int(input())
	c=tuple(input().split())
	s=0
	for a in range (0,x,1):
		d=2*int(c[a])
		if d%3==0:
			s+=d
	print("La suma es",s)
		