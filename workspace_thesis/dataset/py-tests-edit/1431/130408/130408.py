n,m,a,b=map(int,input().split())
if 0<=n<=10000 and 1<=a<=1000 and 1<=b<=1000:
	if a<m<=1000 and b<m<=1000:
		if n!=0:
			if n==1:
				print(b%m)
			else:
				for i in range(2,n,1):
					a,b=b,a+b
					if i==n-1:
						print(b%m)
		else:
			print(a%m)
	