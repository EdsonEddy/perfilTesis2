from sys import stdin
for l in stdin:
	x,y=map(int,(l.split()))#separar una linea
	a,b,m,c=1,x,0,0
	while m!=y:
		c+=1
		m=(a+b)//2
		if m<y:
			a=m+1
		else:
			b=m-1
	print(c)

