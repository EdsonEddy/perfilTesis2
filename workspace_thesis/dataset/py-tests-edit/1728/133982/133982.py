from sys import stdin
for line in stdin:
	n=int(line)
	res=0
	while n>0:
		if n%10&1==0:
			res +=n%10
		n//=10
	print(res)
