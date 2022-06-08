num=str(input())
while True:
	c=0
	sp=int(0)
	si=int(0)
	for i in num:
		c+=1
		if(c%2==0):
			sp+=int(i)
		else:
			si+=int(i)
	if(sp==si):
		print('SI')
	else:
		print('NO')
	num=str(input())
	#print(c)
#num=str(input())
