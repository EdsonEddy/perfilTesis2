while True:
	n=input().split()
	newn=n[1:]
	if int(n[0])==0:
		print("")
	else:
		newn1=newn[::-1]
		for i in range(len(newn1)-1):
			r=newn1[i]
			print(r,end=" ")
		print(newn1[len(newn1)-1])

