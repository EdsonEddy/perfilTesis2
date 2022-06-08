def sum(x):
	sd=0
	while x>0:
		ud=x%10
		sd=sd+ud
		x//=10
	return sd
		
while 1:		
	n,a,b=map(int,input().split())
	s=0
	if n<=10000 and 1<=a<=b<=36:
		for j in range(1, n+1):
			sdd=sum(j)
			if a<=sdd<=b:
				s=s+j
		print(s)