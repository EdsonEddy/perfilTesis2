def suma (v):
	s=0
	for j in range(b,c+1):
		s=s+int(v[j])
	print(s)
n=int(input(""))
for i in range(n):
	a,b,c=(map(int,input().split()))
	x=input()
	v=[]
	v=x.split(" ")
	suma(v)