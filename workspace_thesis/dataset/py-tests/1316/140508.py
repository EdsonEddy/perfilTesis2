import sys
for x in sys.stdin:
	n = int(x)
	A = []
	B = []
	while(len(A)<n):
		A += [int(i) for i in input().split()]
	while(len(B)<n):
		B += [int(i) for i in input().split()]
	ans = 0
	A.sort();
	B.sort();
	for i in range(n):
		ans += B[n-1-i]*A[i]
	print(ans)