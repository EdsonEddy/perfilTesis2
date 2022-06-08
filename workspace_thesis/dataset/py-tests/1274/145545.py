import itertools
from sys import *
for line in stdin:
	cad=line.split()
	cad=cad[1:]
	for i in itertools.combinations(cad,6):
		print(i[0],end='')
		for j in range(1,len(i)):
			print(' ',end=i[j])
		print()