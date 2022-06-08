while True:
	x=int(input())
	n=input().split()
	busc=n[len(n)-1]
	c=0
	for i in range(len(n)):
		if n[i]==busc:
			c+=1
	print(c)