def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)
x=int(input())
for i in range(x):
	a,b,c,d=map(int,input().split())
	num=a*d+b*c
	den=b*d
	div=gcd(num,den)
	print("{}/{}".format((num//div),(den//div)))