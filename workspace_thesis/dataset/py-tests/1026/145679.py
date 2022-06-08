from math import *
from sys import * 
t = int(stdin.readline())
for j in range(t):
	n = int(stdin.readline())
	num = int(sqrt(n*8+1)-1)//2
	ans = (num*(num+1)) // 2
	if(ans == n):
		ans = ('Go On Bob '+str(num))
	else:
		ans = ('Better Luck Next Time')
	stdout.write(ans+'\n')
