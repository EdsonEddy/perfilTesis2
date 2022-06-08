from sys import stdin
for i in stdin:
	a=i.split()
	al=list(a)
	n=int(al[0])
	nl=al[len(al)-1]
	if n==len(al)-1 and n !=0:
		k=0
		e=' '
		for j in range(len(al)-2,0,-1):
			nl=nl+e+al[j]
			#print(al[j])
		print(nl)
	else:
		print()