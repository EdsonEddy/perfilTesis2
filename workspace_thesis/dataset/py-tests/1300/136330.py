from sys import *
for line in stdin:
	l=int(line)
	v=input().split()
	r=v[len(v)-1]
	res=0
	for i in range(len(v)):
		if v[i]==r:
			res+=1
	print(res)