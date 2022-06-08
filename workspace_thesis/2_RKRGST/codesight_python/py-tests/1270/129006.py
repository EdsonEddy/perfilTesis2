from sys import stdin
while 1:
	x=int(input())
	for j in range(x):
		y=int(input())
		if y==0:
			print(1)
		elif y==1:
			print(0)
		else:
			a=y//2
			r=' '
			for k in range( a):
				r=r+str(8)
			if y%2==0:
				print(int(r))
			else:
				r=int(r)
				r=str(4)+str(r)
				print(int(r))