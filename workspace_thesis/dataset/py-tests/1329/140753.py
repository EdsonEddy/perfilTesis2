import sys
for x in sys.stdin:
	n, i, j= map(int,x.split())
	A = []	
	while(len(A)<n):
		A += [int(i) for i in input().split()]	
	#i += 1
	j += 1
	B = A[i:j]
	B.sort()
	A = A[:i]+B+A[j:]
	for i in range(n):
		if(i==n-1):print(A[i])
		else:print(A[i],end=' ')