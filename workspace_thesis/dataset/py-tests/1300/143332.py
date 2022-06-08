from sys import *
for i in stdin:
	n = int(i)
	A = [int(x) for x in input().split()]
	ans = 0
	for c in A:
		if(c==A[-1]):
			ans += 1
	print(ans)