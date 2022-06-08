import sys
for line in sys.stdin:
	v = [int(x) for x in input().split()]
	if len(v)%2 == 0:
		print('-1')
	else:
		print(sorted(v)[len(v)//2])