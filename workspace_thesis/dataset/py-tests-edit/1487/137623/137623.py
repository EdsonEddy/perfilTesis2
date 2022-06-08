from math import sqrt
def primo(p):
	for j in range(3,p,2):
		if p%j==0:
			print('NO ES PRIMO')
			break
	else:
		print('ES PRIMO')
def primom(p):
	for j in range(2,p,1):
		if p%j==0:
			print('NO ES PRIMO')
			break
	else:
		print('ES PRIMO')

while 1:
	n=int(input())
	if n<30 and n>1:
		primom(n)
	elif n==1:
		print('NO ES PRIMO')
	else:
		
		primo(n)