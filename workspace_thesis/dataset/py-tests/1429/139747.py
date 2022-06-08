from sys import *
for line in stdin:
	n,a=map(int,line.split())
	print((n|(1<<a)),(n^(1<<a)))

