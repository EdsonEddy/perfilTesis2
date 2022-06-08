from sys import *
for line in stdin:
	cad1=input()
	cad2=input()
	v=list(map(int,cad1.split(" ")))
	v1=list(map(int,cad2.split(" ")))
	v.sort()
	v1.sort(reverse=True)
	ans=0
	for i in range(len(v1)):
		ans+=v[i]*v1[i]
	print(ans)