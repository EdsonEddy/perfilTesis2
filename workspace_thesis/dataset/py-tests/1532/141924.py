import sys
for n in sys.stdin:
	n=int(n)
	digitos=[ ]
	while(n>0):
		digitos.append(n%10)
		n=n//10
	digitos.sort()
	for i in range (len(digitos)):
		print(digitos[i],end="")
	print("")