import sys
cent = [10,20,50,100,200,500]
dp = [0]*100000
dp[0] = 1
for i in range(5):
	for j in range(cent[i],100000):
		dp[j] += dp[j-cent[i]]
for x in sys.stdin:	
	ans = ''
	for c in x:
		if(c=='\n'):
			continue
		ans += c
	m, s = x.split()
	n = (float(m)*100)
	if(n%10!=0):
		print("No existe forma de producir cambio exacto.")
		continue
	n = int(n)
	if(dp[n]==1):
		print("Existe solo 1 manera de producir "+ans+" de cambio.")
	else:
		print("Existen "+str(dp[n])+" maneras de producir "+ans+" de cambio." )

