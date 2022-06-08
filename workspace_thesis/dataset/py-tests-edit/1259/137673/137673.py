from sys import stdin
for i in stdin:
	b,n=map(int,i.split())
	if b==0 and n==0:
		break
	else:
		c=0
		if b>=2 and n>=1:
			while n>=b :
				n//=b
				c+=1
			print(c)