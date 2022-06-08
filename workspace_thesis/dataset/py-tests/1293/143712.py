cas=int(input())
while cas>0:
	a,b=map(int,input().split())
	n=input().split()
	s=0
	for i in range(a,b+1):
		s=s+int(n[i])
	print(s)
	cas-=1