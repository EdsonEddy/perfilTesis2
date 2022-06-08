v=[0,1,1]
for i in range(3,41):
	v.append(v[i-3]+v[i-2]+v[i-1])
n=int(input())
for i in range(n):
	res=0
	x=int(input())
	for j in range(1,x):
		res+=v[j]
	print(res)