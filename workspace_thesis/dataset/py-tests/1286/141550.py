t=int(input())
for i in range(t):
	cad=input()
	v=list(map(int,cad.split()))
	ans=0
	for j in range(1,len(v)):
		if v[j]>v[j-1]:
			ans+=1
	print(ans)

