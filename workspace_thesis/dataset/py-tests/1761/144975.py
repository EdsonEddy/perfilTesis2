import sys
N = 40000
dp = [0]*N
cent = [5,10,20,50,100,200,500,1000,2000,5000,10000]
dp[0] = 1
for c in cent:
	for i in range(c,N):
		dp[i] += dp[i-c]
num = '1234567890'
while (1):
	x =sys.stdin.readline() 
	n = ''
	for i in x:
		if(i in num):
			n += i
	n = int(n)
	if(n==0):
		break	
	print("{:6.2f}{:17d}".format(n/100,dp[n]))
