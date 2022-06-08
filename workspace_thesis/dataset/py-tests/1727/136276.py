l,r,k=map(int,input().split())
res=0
for i in range(l,r+1):
	if i%k==0:
		res+=1
print(res)