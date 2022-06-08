x=input()
l=len(x)
lis=[""]*l
for i in range(l):
	lis[i]=(x[i:l])
lis.sort()
print(*lis,sep="\n")