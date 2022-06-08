import math

cont = True
while cont:
	k = int(input())
	if k > 0:
		cont = False
n = 0 
for i in range(1, k+1):
	s1 = int(math.pow(2, (math.pow(2, n)))+1)
	n = n + 1
	if i == k:
		print(s1)
	else:
		print(s1, end=' ')
