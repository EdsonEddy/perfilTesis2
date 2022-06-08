
n=int(input())
v=list(map(int,input().split()))
aux=[]
sw=0
a=0
aux=[v[i] for i in range(len(v))]
for j in range(n):
	if(aux[j]>=a):
		a=aux[j]
		sw=j
	else:
		break
for k in range(sw+1,n):
	if(aux[k]<a):
		a=aux[k]
		sw=k
	else:
		break
if(sw==n-1):
	print("SI")
else:
	print("NO")