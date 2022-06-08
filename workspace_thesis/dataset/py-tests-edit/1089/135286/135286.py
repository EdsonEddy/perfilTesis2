import math
n = int(input())
l = int(math.log10(n))
l= l+1
if l%2==0:
	print("*")
else:
	l = (l//2)+1
	for i in range (l):
		j = n%10
		n = int(n/10)
	print(j)
