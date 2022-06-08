x=int(input())
for i in range(1,x+1,1):
	a,b=map(int,input().split(" "))
	if (a==b):
		print("=")
	elif(a>b):
		print(">")
	else:
		print("<")