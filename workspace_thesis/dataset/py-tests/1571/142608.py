from sys import *
for l in stdin:
	n=int(l)
	cad=input()
	v=list(map(int,cad.split()))
	ans=0
	for i in range(1,len(v)-1):
		if (v[i-1]<v[i] and v[i]>v[i+1]) or (v[i-1]>v[i] and v[i]<v[i+1]):
			ans+=1
	print(ans) 
