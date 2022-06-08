v=[1,1]
m=1000000007
for i in range(2,100002,1):
	v.append((v[i-2]%m+v[i-1]%m)%m)
n=int(input())
print(v[n-1])