n=1
while n!=0:
	n=int(input())
	if n==0:
		break
	else:
		s=input().split()
		c=0
		for i in s:
			k=int(i)
			c=c+k
		print(c)