from sys import stdin
from math import log10
while 1:
	n=int(input())
	ln=int(log10(n)+1)
	si,sp=0,0
	for j in range (ln):
		if j%2==0:
			ud=n%10
			sp+=ud
			n//=10
		else:
			ud=n%10
			si+=ud
			n//=10
	if sp==si:
		print('SI')
	else:
		print('NO')