from sys import *
for i in stdin:
	A = [int(x) for x in i.split()]
	A = A[1:]
	if(len(A)):
		print(*reversed(A))
	else:print()