from math import*
b=int(input())
for j in range(1,b+1,1):
	n,k=map(int,input().split())
	c=int(log(n,10))
	for i in range(1,k+1,1):
		d=n//10**c
		n=n%10**c
		n=n*10+d
	print(n)