import sys
for line in sys.stdin:
	v = list(map(int, input().split()))
	print(max(v)-min(v))