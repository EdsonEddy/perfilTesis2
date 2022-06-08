while True:
	n=int(input())
	l=[]
	for i in range (n):
		x=input()
		x=x[::-1]
		l.insert(0,x)
	for j in range(len(l)):
		print(l[j])