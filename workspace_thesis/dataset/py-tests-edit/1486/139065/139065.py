n=int(input())
b=0
x=1
for i in range(1,n+1):
	if i%2==0:
		print(i)
	else:
		d=x+b
		print(d)
		x=b
		b=d