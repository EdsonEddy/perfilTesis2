while 1:
	n= int(input())
	numer=input().split()
	verval=input().split()
	lnu=list(numer)
	lver=list(verval)
	p=[ ]
	s=0
	for j in range(n):
		s=s+int(lnu[j])+int(lver[j])
		p.append( int(lnu[j])+int(lver[j]))
	cp=s/n
	c=0
	for k in p:
		if k<cp:
			c+=1
	print(c)