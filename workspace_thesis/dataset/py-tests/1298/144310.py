from sys import stdin
for line in stdin:
	sec = list(map(int, line.split()))
	for i in range(sec[0], 1, -1):
		print(sec[i], end=' ')
	if sec[0] != 0:
		print(sec[1])
	else:
		print()