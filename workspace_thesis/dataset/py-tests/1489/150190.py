import sys
v = [0]
for n in range(101):
	v.append(v[n]+n*(n+3)//2+1)
for line in sys.stdin:
	print(v[int(line)])