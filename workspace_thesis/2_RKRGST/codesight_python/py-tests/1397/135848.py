def numdosb(n) : 
	x = 1
	while (n > 0) : 
		y = 0
		while (y < x) :
			if (n-1)!=0:
				print((1*2**x) + (1*2**y), end = " " )
			else:
				print((1*2**x) + (1*2**y), end = "\n" )
			n-=1
			if (n == 0) : 
				return
			y += 1
		x += 1
while True:
	a=input()
	if a=="":
		break
	else:
		a=int(a)
		numdosb(a)