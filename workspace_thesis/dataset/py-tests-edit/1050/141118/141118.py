while True:
	n = int(input())
	m = bin(n)[2:]
	inv = m[::-1]
	print(int(inv,2))