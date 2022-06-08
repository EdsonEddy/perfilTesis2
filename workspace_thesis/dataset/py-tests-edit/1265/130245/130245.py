from sys import stdin
for a1 in stdin:
	a=int(a1)
	print("({}, {}, {})".format(a//240,(a%240)//12,(a%240)%12))