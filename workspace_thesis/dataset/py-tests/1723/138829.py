import sys
for x in sys.stdin:
	a, b = map(int,x.split())
	sw = 0
	while(a>0):
		if(a%10!=b%10):sw += 1
		a = a//10
		b = b//10
	if(sw>1):print('lentes')
	else: print('feliz')
