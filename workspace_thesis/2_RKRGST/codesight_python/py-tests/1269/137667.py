while 1 :
	n1,d1,n2,d2=map(int,input().split())
	if  d1 >= 1 and d2 >= 1 and n1>=1 and n2>=1:
		if n1/d1==n2/d2:
			print('=')
		else:
			print('!=')
	else:
		break