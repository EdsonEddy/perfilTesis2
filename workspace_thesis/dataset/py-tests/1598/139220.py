import math
import sys
criba = [0]*1000010
for i in range(2,500005):
	if(criba[i]==0):
		j = i
		while(j<1000010):
			criba[j] += i
			j += i
for i in sys.stdin:
	a, b = map(int,i.split())	
	for j in range(a,b):
		if(criba[j]==criba[j+1]):
			print(j,j+1)
