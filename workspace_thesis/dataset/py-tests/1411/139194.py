import sys
import math

for x in sys.stdin:
	a, b = map(int,x.split())
	b %= 8
	i = 7
	s =''
	while(i>=0):
		if(a&(1<<i)):s+=('1')
		else:s+=('0')
		i -= 1		
	s = s[b:]+s[:b]	
	c=0
	i = 7	
	while(i>=0):
		if(s[7-i]=='1'):c+=(1<<i)
		i -= 1
	print(c)
