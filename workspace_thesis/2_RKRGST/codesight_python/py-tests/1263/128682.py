from sys import stdin
for i in stdin:
	ls,n=map(int,i.split())
	c=1
	li=1
	while 1:
		x=(li+ls)//2
		if x==n:
			break
		elif x>n:
			ls=x-1
		else:
			li=x+1
		c+=1
	print(c)
		
	