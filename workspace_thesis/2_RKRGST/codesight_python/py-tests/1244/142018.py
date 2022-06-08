from math import pi 
n=int(input())
for i in range(n):
	v=input().split()
	if v[0]=='rectangle':
		a=int(v[1])*float(v[2])
		print("{0:.2f}".format(a))
	elif v[0]=='circle':
		a=pi*(int(v[1]))**2
		print("{0:.2f}".format(a))