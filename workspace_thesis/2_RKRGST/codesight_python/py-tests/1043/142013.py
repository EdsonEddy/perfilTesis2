n=int(input())
for i in range(n):
	c,p=map(int,input().split())
	r,t=c//3,p//2
	if r<t:
		w=p-r*2
		x=c%3
		z=w+x
		print(r,z)
		
	else:
		w=c-t*3
		x=p%2
		z=w+x
		print(t,z)