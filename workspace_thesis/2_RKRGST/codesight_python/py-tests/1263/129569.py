import math
while (True):
	try:
		a,b=input().split()
		a,b=int(a),int(b)
		ini=1
		inte=1
		x=(ini+a)/2
		x=int(math.floor(x))
		while (x!=b):
			if x<b:
				x=x+1
				ini=x
			else:
				x=x-1
				a=x
			inte=inte+1
			x=(ini+a)/2
			x=int(math.floor(x))
		print(inte)
	except:
		break