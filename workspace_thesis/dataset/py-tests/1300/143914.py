while True:
	n=int(input())
	s=tuple(input().split())
	d=s[n-1]
	c=s.count(d)
	print(c)