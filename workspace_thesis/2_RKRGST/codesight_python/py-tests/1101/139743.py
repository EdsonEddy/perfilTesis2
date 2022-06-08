x=int(input())
for i in range(x):
	a,b=map(int,input().split())
	ans=0
	while a>0 and b>0:
		if a>=b:
			ans+=a//b
			a%=b
		else:
			ans+=b//a
			b%=a
	print(ans)
