x=int(input())
if(x>=10 and x<=30):
	print("esta bien")
elif (x<10):
	print("hace frio")
	if (x<=0):
		print("se congela")
elif (x>30):
	print("hace calor")
	if (x>=100):
		print("hierve")