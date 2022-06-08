from sys import stdin
for l in stdin:
	x=int(l)
	c1,c2,sw=0,0,1
	while x>0:
		if sw==1:
			c1+=x%10
			sw=33
		else:
			sw=1
			c2+=x%10
		x//=10
	if c1==c2:
		print("SI")
	else:
		print("NO")


