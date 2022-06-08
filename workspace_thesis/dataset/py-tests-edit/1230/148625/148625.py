a=int(input())
h,m=0,0
if a>3600:
	h=a//3600
	a%=3600
if a>60:
	m=a//60
	a%=60
print(h,m,a)