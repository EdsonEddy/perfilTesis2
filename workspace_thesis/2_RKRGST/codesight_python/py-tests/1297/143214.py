while True:
	x=input()
	if x!="":
		x=int(x)
		for i in range(x):
			n=str(input())
			print(n[::-1])
	else:
		break