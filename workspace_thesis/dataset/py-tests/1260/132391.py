def mcd(a,b):
	r=0
	while (b>0):
		r=b
		b=a%b
		a=r
	return a
n=int(input())
for i in range(1,n+1,1):
	x,y=map(int,input().split())
	print(mcd(x,y))
	