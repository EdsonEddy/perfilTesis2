n = int(input())
for i in range(0,n):
	m = int(input())
	l = list(map(int,input().split()))
	l.sort()
	print(*l)