from sys import *
N=100010
v=list(range(N))
r=list(range(N))
i=2
while i*i<N:
	if v[i]==i:
		j=i*i
		while j<N:
			if v[j]==j:
				v[j]=i
			j+=i
	i+=1

for i in range(2,N):
	a=1
	j=i
	y=v[j]
	while j!=1:
		if y!=v[j]:
			a+=1
			y=v[j]
		j//=v[j]
	r[i]=a

for line in stdin:
	n,a=map(int,line.split())
	may=-1
	primo=0
	for i in range(n,a+1):
		if may<=r[i]:
			primo=i
			may=r[i]
	print("{} tiene {} divisores".format(primo,may))



