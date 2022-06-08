while True:
	a=int(input())
	l=[]
	for i in range (a):
		n=input()
		n=n[::-1]
		l.insert(0,n)
	for i in range(len(l)):
		print(l[i])