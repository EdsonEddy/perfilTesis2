n=int(input())
for i in range (n):
	x=input()
	y=input()
	v=[0 for a in range (260)]
	flag=True
	for j in range(len(x)):
		v[ord(x[j])]+=1
	for j in range(len(y)):
		v[ord(y[j])]-=1
		if (v[ord(y[j])]<0):
			flag=False
	if (flag==True):
		print("Si")
	else:
		print("No")
		