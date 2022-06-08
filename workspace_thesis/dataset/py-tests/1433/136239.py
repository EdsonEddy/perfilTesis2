a,b=map(int,input().split())
res=0
for i in range(a,b+1):
	sw=True
	for j in range(2,i):
		if i%j==0:
			sw=False
			break
	if sw==True and i!=1:
		res+=1
print(res)

