from math import *
from sys import stdin
for l in stdin:
	l1=int(l)
	cv,ch=0,0
	x,y,z=map(int,input().split())
	if fabs(x)>0 and x<l1:
		cv+=1
	if fabs(y)>0 and y<l1:
		cv+=1
	if fabs(z)>0 and z<l1:
		cv+=1
	x,y,z=map(int,input().split())
	if fabs(x)>0 and x<l1:
		ch+=1
	if fabs(y)>0 and y<l1:
		ch+=1
	if fabs(z)>0 and z<l1:
		ch+=1

	print((cv+1)*(ch+1))