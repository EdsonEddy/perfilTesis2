import sys
while True:
	b=input()
	if b!="":
		b=int(b)
		ci=0
		cp=0
		c=1
		while(b>0):
			aux=b%10
			b=int(b/10)
			if c%2==0:
				cp=cp+aux
			else:
				ci=ci+aux
			c=c+1
		if ci==cp:
			print("SI")
		else:
			print("NO")
	else:
		sys.exit()