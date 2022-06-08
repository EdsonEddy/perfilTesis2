from sys import *
def capicua(n):
	capi,nn=0,n
	while n>0:
		capi = capi*10+(n%10)
		n//=10
	if nn==capi:
		return True
	return False
for line in stdin:
	x=int(line)
	ans=0
	for i in range(x):
		y=int(input())
		if capicua(y)==True:
			ans+=1
	print(ans)
