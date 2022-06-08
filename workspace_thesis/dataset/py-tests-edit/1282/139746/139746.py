from sys import *
N=10021
v=list(range(N))
v[0]=v[1]=1
i=2
while i<N:
	if v[i]==i and i<N:
		j=i+i
		while j<N:
			v[j]=i
			j+=i
	i+=1

for line in stdin:
	n=int(line)
	print(v[n])

