while 1:
	n=int(input())
	c=input().split()
	nc=c[:n]
	ue=nc[n-1]
	c=0
	for i in nc:
		if i == ue:
			c+=1
	print(c)