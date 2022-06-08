import math
import sys
criba = [1]*1000501
i=3
criba[1]=0
while(i*i<=1000500):
	if(criba[i]):
		j = i*i
		while(j<=1000500):
			criba[j] = 0
			j += i
	i += 2
mod = 1000007
n = int(input())
a = 1
b = 3
first = 1
for i in range(n):
	if(a==2 or (criba[a] and a%2)):
		if(first):
			print(a,end='')
			first = 0
		else:
			print(' '+str(a),end='')
	c = (a%mod + b%mod) % mod
	a = b
	b = c
	
print()
