from sys import *
for line in stdin:
	n=int(line)
	v=[]
	while n>0:
		v.append(n%10)
		n//=10
	v.sort()
	for i in range(len(v)):
		print(v[i],end="")
	print()	
