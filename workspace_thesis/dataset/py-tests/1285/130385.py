a=0
while a!=" ":
	a=input()
	k=0
	g=0
	for i in range(0,len(a),2):
		b=int(a[i])
		k=k+b
		#print(k)
	for u in range(1,len(a),2):
		c=int(a[u])
		g=g+c
		#print(g)
	if k==g:
		print('SI')
	else:
		print('NO')