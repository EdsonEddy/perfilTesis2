x=str(input())
y=str(input())
au=int(x.find(y))
c=0
while au!=-1:
	print(au+c)
	x=x[0:au]+x[au+1:len(x)]
	au=int(x.find(y))
	c+=1