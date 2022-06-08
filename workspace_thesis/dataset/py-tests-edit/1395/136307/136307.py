from sys import *
from math import *
for line in stdin:
	l=int(line)
	r=0.0
	for i in range(1,l+1):
		r+=log10(i)
	print(int(r)+1)
