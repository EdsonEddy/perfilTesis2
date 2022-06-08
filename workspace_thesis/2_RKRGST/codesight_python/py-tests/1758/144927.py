import sys

cart = [1,5,8,14]
N = 10010
INF = 1<<30
dp=[INF]*N
dp[0]=0
for i in cart:
	for j in range(i,N):
		dp[j] = min(dp[j],1+dp[j-i])

for x in sys.stdin:	
	n = int(x)
	if(n==-1):
		break
	print(dp[n])
