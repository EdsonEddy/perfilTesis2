from sys import *
while(1):
	n = int(stdin.readline())
	A = []
	while(len(A)<n):
		x ,y =stdin.readline().split("\n")
		A += list(map(int,x.split()))
	x = int(stdin.readline())
	i = 0
	n -= 1
	A.sort()
	while(n>i):
		if(A[i]+A[n]==x):break
		if(A[i]+A[n]<x):i += 1
		else: n -= 1
	if(i<n):print(A[i],A[n])
	else: print(-1)