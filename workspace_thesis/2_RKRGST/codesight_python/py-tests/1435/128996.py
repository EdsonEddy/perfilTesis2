from math import log10
n,k=map(int,input().split())
cd=int(log10(n)+1)
nn=n
c=' '
if k<=cd:
	for i in range (cd):
		ud=nn%10
		c=c+str(ud)
		nn//=10
	nn=int(c)
	for j in range(k-1):
		nn=nn//10
	ud=nn%10
	print(cd,ud)
	