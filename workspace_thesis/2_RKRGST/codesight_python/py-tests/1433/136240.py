v=list(range(1002))
for i in range(len(v)):
	v[i]=0

v[0]=v[1]=1
i=2
while i*i<1002:
	if v[i]==0:
		j=i*i
		while j<1002:
			v[j]=1
			j+=i
	i+=1
a,b=map(int,input().split())
res=0
for i in range(a,b+1):
	if v[i]==0:
		res+=1
print(res)