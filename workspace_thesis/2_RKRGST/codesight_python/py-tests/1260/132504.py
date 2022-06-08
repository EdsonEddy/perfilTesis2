n=int(input())
for i in range(n):
	a,b = map(int,input(). split())
	r=0
	while b>0:
		r=b
		b,a= a%b,r
	if b==0:
		print (a)