x=int(input())
for i in range(x):
	a,b=input().split()
	a,b=int(a),int(b)
	c=a%3+b%2
	da=a//3
	db=b//2
	r=da
	if da>db:
		r=db
		c=c+(da-db)*3
	else:
		c=(db-da)*2+c
	print(r,c)