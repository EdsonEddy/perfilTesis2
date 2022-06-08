t = int(input())
for i in range(t):
	a, b = map(int,input().split())
	A = list(map(int,input().split()))
	print(sum(A[a:b+1]))