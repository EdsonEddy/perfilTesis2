from sys import *
for x in stdin:
	n = int(x)
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	prom = (sum(A)+sum(B))/n
	ans = 0
	for i in range(n):
		if(A[i]+B[i]<prom):
			ans += 1
	print(ans)