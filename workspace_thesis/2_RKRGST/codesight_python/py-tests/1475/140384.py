n,a,b=map(int,input().split())
x=input().split()
for i in range(a):
	print(x[i])
for i in range(b,a-1,-1):
	print(x[i])
for i in range(b+1,n):
	print(x[i])