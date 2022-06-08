from sys import *
for line in stdin:
	n=int(line)
	cad=input()
	v=list(map(int,cad.split()))
	cad=input()
	v1=list(map(int,cad.split()))
	v.sort()
	v1.sort(reverse=True)
	ans=0
	for i in range(len(v)):
		ans+=v[i]*v1[i]
	print(ans)