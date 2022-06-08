n=0
while n!='':
	g=int(input())
	a=input().split()
	x=[int(k) for k in a]
	s=0
	for i in x:
		if i==x[len(x)-1]:
			s=s+1
	print(s)