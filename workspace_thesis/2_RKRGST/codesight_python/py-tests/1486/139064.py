n=int(input())
a=1
b=0
for i in range(1,n+1):
	if i%2==0:
		print(i)
	else:
		d=a+b
		print(d)
		a=b
		b=d