cdp = int(input())
for casos in range(0,cdp):
	elem, bonacc = map(int,input().split())
	bon = [1]*bonacc
	c, s, nl = 0,0,[]
	while c<elem:
		for i in bon:
			s = s+i
		bon.append(s)
		bon.remove(bon[0])
		s=0
		c=c+1
	print(bon[0])