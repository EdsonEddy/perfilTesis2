x,y=map(int,input().split())
ini,fin=0,0
if x>y:
	ini=x
	fin=y
else:
	ini=y
	fin=x
for i in range(ini,fin-1,-1):
	print(i)
