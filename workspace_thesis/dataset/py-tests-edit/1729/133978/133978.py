from sys import stdin
for line in stdin:
	n=int(line)
	res,p=0,1
	while n>0:
		if n%10&1==0:
			res += p*(n%10)
			p*=10
		n//=10
	print(res)
