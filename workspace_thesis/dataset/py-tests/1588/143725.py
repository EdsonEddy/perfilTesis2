n=int(input())
for i in range(n):
	x=int(input())
	y=input().split()
	yi=[int(w) for w in y]
	s=0
	for j in range(x):
		if yi[j]%3==0:
			s=s+2*yi[j]	
	print('La suma es',s)