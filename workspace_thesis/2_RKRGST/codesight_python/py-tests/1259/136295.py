from sys import *
from math import *
for line in stdin:
	a,n=map(int,line.split())
	print(int(log10(n)/log10(a)))