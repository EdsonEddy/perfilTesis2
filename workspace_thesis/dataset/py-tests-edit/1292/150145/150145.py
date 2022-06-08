import sys
for line in sys.stdin:
	if int(line) == 0:
		break
	print(sum(map(int, input().split())))