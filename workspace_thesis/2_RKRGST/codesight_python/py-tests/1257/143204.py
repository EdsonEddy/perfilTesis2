t=int(input())
for i in range(t):
	c1=input()
	c=input()
	v=[0 for i in range(26)]
	for i in range(len(c1)):
		if c1[i]!=' ':
			v[ord(c1[i])-97]+=1
	for i in range(len(c)):
		if c[i]!=' ':
			v[ord(c[i])-97]+=1
	flag=1
	for i in range(len(v)):
		if (v[i]&1)==1:
			flag=0
			break
	if flag:
		print("Si")
	else:
		print("No")