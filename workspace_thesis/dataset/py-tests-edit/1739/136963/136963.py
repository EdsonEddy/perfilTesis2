from sys import *
v=[35  ,8 , 43  ,7  ,50  ,5  ,55  ,10  ,65  ,11]
for line in stdin:
	l=int(line)
	for i in range(l):
		print(v[i],end="")
		if i+1!=l:
			print(end="  ")
	print()