while 1:
	n=input()
	if n=="fin":
		break
	n1=int(n)
	res=0
	for i in range(n1):
		x=int(input())
		res+=x
	print(res)

