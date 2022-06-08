n=int(input())
a,b=1,1
for i in range(n):
	r=a*b
	a+=1
	b=r
	if i%2==0:
		print(-r)
	else:
		print(r) 