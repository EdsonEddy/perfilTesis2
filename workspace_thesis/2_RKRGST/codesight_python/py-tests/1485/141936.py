def pal(n):
	au,nn=n,0
	while au>0:
		nn=au%10+nn*10
		au=au//10
	if nn==n:
		return 1
	else:
		return 0

while True:
	x=input()
	if x!="":
		x=int(x)
		con=0
		for i in range(x):
			n=int(input())
			if pal(n)==1:
				con+=1
		print(con)
	else:
		break