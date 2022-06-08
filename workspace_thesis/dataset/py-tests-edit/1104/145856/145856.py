from sys import *
while(1):
	x = stdin.readline()
	if(x=='\n'):continue
	x, y = x.split("\n")	
	n, m = map(int,x.split())
	if(n == 0 or m == 0):
		break
	m = 1 + n - m 
	n = (n*(n+1))
	m = (m*(m+1))
	ans = (n-m)//2
	stdout.write(str(ans)+'\n')