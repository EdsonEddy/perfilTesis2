num_rep = int(input())
for chiste in range(0,num_rep):
	num_ins = int(input())
	c, blah = 0, 0
	for homero in range(0,num_ins):
		ins = input()
		if ins != 'porque' and blah != 1:
			c=c+1
		elif ins == 'porque':	
			blah = 1
	print(c)