x=input()
x = x.lower()
for i in range(len(x)):
	if x[i]!='a' and x[i]!='e' and x[i]!='i' and x[i]!='o' and x[i]!='u' and x[i]!='y':
		print('.',end=x[i])
