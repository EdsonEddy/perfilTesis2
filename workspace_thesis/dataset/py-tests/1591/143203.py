pri=[2,3,5,7]
x=int(input())
for u in range(x):
	n=int(input())
	nn=0
	d=0
	while n>0:
		aux=n%10
		if aux in pri:
			nn=nn+(aux*10**d)
			d=d+1
		n=n//10
	if nn!=0:
		print(nn)
	else:
		print("-1")