n=int(input())
for i in range(n):
	a,b=map(int,input().split())
	if (2<=a,b<=10**5):
		for i in range(1,b+1):
			if (a%i==0 and b%i==0 and a%i==b%1):
				mcd=i
		print(mcd)
	