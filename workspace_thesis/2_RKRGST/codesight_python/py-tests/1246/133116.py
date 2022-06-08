j=str(input())
a=str(input())
i=0
c=0
while i>=0:
	b=a.find(j,i)
	if b<0:
		break
	c=c+1
	i=b+1
print(c)

