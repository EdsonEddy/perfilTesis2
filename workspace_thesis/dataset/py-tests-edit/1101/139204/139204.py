def gcd(a,b):
	if(a%b==0):
		return a//b
	return gcd(b,a%b)+(a//b)
t = int(input())
for i in range(t):
	a, b = map(int,input().split())
	print(gcd(a,b))