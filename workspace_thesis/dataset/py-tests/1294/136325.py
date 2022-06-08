t=int(input())
for i in range(t):
	n,a,b=map(int,input().split())
	l=input().split()
	r=0
	for i in range(len(l)):
		if i>=a and i<=b:
			r+=int(l[i])
	print(r)
	