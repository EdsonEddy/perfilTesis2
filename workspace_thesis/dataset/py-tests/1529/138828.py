import math
t = int(input())
for i in range(t):
	n, k = map(int,input().split())
	m = int(math.log10(n))+1
	k %= m
	a = 10**(m-k)
	b = 10**k
	n = (n%a)*b + (n//a)
	print(n)
