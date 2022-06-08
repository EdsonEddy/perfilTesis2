n=int(input())
p="2357"
for i in range(n):
	t=str(input())
	c=0
	r=""
	for a in t:
		if a in p:
			r+=a
			c+=1
	if c==0:
		print(-1)
	else:
		print(r)