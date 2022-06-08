import math
t = int(input())
for i in range(t):
	n = int(input())
	n = int(math.log(n)/math.log(2)) + 1
	print(n)