import sys
for x in sys.stdin:
	n = int(x)
	i = 1
	print('Divisores de '+str(n)+':',end='')
	while(i*i<n):
		if(n%i==0):
			print('',i,end='')
		i += 1
	if(i*i==n):print('',i,end='')
	i -= 1
	while(i>0):
		if(n%i==0):
			print('',(n//i),end='')
		i -= 1
	print()
