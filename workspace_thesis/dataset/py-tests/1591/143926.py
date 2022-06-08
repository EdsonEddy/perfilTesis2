n=int(input())
for n in range(n):
	a=str(input())
	p=[2,3,5,7]
	c=""
	for k in a:
		if int(k) in p:
			c=c+k
	if c=="":
		print("-1")
	else:
		print(c)