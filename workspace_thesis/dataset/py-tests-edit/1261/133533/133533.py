n = int(input())
for i in range (1, n+1):
	a, b = map(int, input().split())
	a = a**b
	print (a)