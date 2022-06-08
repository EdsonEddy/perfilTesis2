n=int(input())
for i in range(n):
	a,b=map(int,input().split())
	s1=0
	s2=0
	while a>0:
		ud=a%10
		s1=s1+ud
		a//=10
	while b>0:
		ud=b%10
		s2=s2+ud
		b//=10
	if s1>s2:
		print(s1)
	else:
		print(s2)