import sys
import math
n=int(input())
for x in range (n):
	
	n, k = map (int,input().split())
	cd=1

	if n>0:
		cd=int(math.log10(n))+1
	k = k%cd 
	m=10**(cd-k)
	n=(n%m)*(10**k) + (n//m)
	print(n)	
