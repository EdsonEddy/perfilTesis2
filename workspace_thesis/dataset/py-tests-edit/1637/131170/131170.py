n,m,l=map(int,input().split())
k,j,h=map(int,input().split())
if n+k ==5:
	if m+j==5:
		if l+h==5:
			print ("Esta es la llave")
		else:
			print ("Intenta con otra")
	else:
		print ("Intenta con otra")
else:
	print ("Intenta con otra")
