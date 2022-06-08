from math import *
g=int(input())
for k in range(g):
	s=input().split()
	l=[]
	for i in s:
		l.append(i)
	if l[0]=='circle':
		a=pi*float(l[1])**2
	else:
		a=float(l[1])*float(l[2])
	print("{0:.2f}".format(a))