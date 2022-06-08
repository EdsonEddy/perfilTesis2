import sys
v3 , v4 , v5 = [1], [1], [1]
for i in range(1, 101):
	v3.append(v3[i-1] + i+1)
for i in range(1, 102):
	v4.append((i+1)**2)
for i in range(101):
	v5.append(v3[i]+v4[i+1])
for line in sys.stdin:
	print(*v5[:int(line)])