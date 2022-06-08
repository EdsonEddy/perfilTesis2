from sys import stdin

def sumDig(x):
	s = 0
	while x != 0:
		s += x % 10
		x //= 10
	return s

for line in stdin:
	s = 0
	n, a, b = map(int, line.split())
	if n <= 10000 and 1 <= a <= b <= 36:
		for i in range(1, n+1):
			if a <= sumDig(i) <= b:
				s += i
		print(s)
