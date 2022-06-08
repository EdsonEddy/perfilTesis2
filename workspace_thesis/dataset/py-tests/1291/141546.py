from sys import *
for line in stdin:
	v=list(map(int,line.split()))
	ans=0
	for i in range(len(v)):
		ans+=v[i]
	print(ans)