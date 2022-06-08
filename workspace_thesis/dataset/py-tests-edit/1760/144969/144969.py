import sys
N = 10000
dp = [0]*N
losas = [100,400,900,1600,2500]
dp[0] = 1
for los in losas:
	for i in range(los,N):
		dp[i] += dp[i-los]
for x in sys.stdin:
	n = int(x)
	if( n%100==0 ):
		print(dp[n])
	else:
		print('AREA NO VALIDA')