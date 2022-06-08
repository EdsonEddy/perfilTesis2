import math
n=int(input())
cd=int(math.log10(n))+1
if cd%2==0:
	print("*")
else:
	print((n//(10**(cd//2)))%10)
