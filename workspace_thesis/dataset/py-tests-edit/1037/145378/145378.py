n=int(input())
for i in range(n):
	v=[0 for i in range(26)]
	c1=input()
	c=0
	c2=input()
	for j in range(len(c1)):
		v[ord(c1[j])-97]+=c
		c+=1
	ans=0
	for j in range(len(c2)-1):
		ans+=abs(v[ord(c2[j])-97]-v[ord(c2[j+1])-97])
	print(ans)


