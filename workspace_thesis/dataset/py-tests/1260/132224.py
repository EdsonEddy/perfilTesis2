x=int(input())
for i in range(x):
	a,b=map(int,input().split())
	if a>b:
		aux=a
		a=b
		b=aux
	for j in range(a,0,-1):
		if a%j==0 and b%j==0:
			print(j)
			break