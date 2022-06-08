n,a,b=map(int,input().split())
cad=input()
v=list(map(int,cad.split()))
v1=v[:a]
v2=v[a:b+1]
v3=v[b+1:]
v2.sort()
v1=v1+v2+v3
for i in range(len(v1)):
	print(v1[i],end="")
	if i+1!=len(v1):
		print(end=" ")
