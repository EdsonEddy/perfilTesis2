casos=int(input())
while casos>0:
	cas1=int(input())
	a=input().split()
	b=[int(x) for x in a]
	s=0
	for i in range (len(b)):
		if b[i]%3==0:
			s=s+b[i]*2
	print("La suma es",s)
	casos-=1