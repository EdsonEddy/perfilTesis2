import math
k=int(input())
for j in range(1,k+1,1):
	n=int(input())
	l=int(math.log10(n))+1
	nw=0
	p=0
	for i in range(1,l+1,1):
		d=n%10
		n=n//10
		if(d==2 or d==3 or d==5 or d==7):
			nw=nw+(d*(10**p))
			p=p+1
	print(nw)