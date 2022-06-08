n=int(input())
for n in range(n):
	o=int(input())
	a=input().split()
	k=[int(i) for i in a]
	s=0
	for g in k:
		if (g*2)%3==0:
			s=s+g*2
	print("La suma es",s)