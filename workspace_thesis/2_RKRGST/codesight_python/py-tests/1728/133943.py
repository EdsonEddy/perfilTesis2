from sys import stdin
for line in stdin:
	l=int(line)
	res=0
	while l>0:
		if (l%10)&1==0:
			res+=l%10
		l//=10
	print(res)
