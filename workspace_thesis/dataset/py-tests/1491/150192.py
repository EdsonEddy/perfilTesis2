import sys
for line in sys.stdin:
	S, D = list(map(int, line.split()))
	x = S//(2**D-1)
	print("%s=%d" % ('+'.join([str(x*2**e) for e in range(D)]), S))