from sys import stdin
for l in stdin:
	ll=input()
	lll = ll.split()
	may,mini=-1,100000000
	for i in range(len(lll)):
		x= int(lll[i])
		if may<x:
			may=x
		if mini>x:
			mini=x
	print(may-mini)
	
	