from sys import *
for l in stdin:
	n=int(l)
	cad=input()
	v=list(map(int,cad.split()))
	ans=0
	v.sort()
	for i in range(len(v)):
		ans=max(v[i]*(n-i),ans)
	print(ans) 
