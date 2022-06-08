t=int(input())
for i in range(t):
	n=int(input())
	l=input().split()
	r=0
	for i in range(len(l)):
		r+=int(l[i])
	print(r)
	