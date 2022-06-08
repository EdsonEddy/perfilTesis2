from sys import *
for line in stdin:
	v=input().split()
	x=v[len(v)-1]
	ans=0
	for i in range(len(v)):
		if v[i]==x:
			ans+=1
	print(ans)

	