import math
import sys
criba = [1]*10000
for i in range(2,10000):
	if(criba[i]==1):
		j = i
		while(j<10000):
			criba[j] = i
			j += i
for i in sys.stdin:
	n = int(i)	
	print(criba[n])
