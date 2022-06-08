while True:
	x=str(input())
	if x!="end":
		sw,acep,ac,y,sa=0,0,0,len(x),0
		for i in range(y):
			c=x[i:(i+1)]
			if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
				acep+=1
				ac=0
				sa=1
			else:
				acep=0
				ac+=1
			if c==x[i-1:(i)]:
				sw=1
				if c=="e" and x[(i-1):i]=="e" or c=="o" and x[(i-1):i]=="o":
					sw=0
			if sw==1 or acep==3 or ac==3:
				sw=1
				break
		if sw==1  or sa==0:
			print("<",x,">"," is not acceptable.",sep="")
		else:
			print("<",x,">"," is acceptable.",sep="")
	else:
		break