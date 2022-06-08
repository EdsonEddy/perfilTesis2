n=int(input())
s=0
f=1
for i in range(n):
	a=int(input())
	aa=a
	while a>0:
		ud=a%10
		a//=10
		for j in range(1,ud+1,1):
			f*=j
		s+=f
		f=1
	if s==aa:
		print('Y')
		s=0
	else:
		print('N')
		s=0