t=int(input())
for i in range(t):
	l=input().split()
	r=0
	for i in range(len(l)):
		r+=int(l[i])
	print(r)
	