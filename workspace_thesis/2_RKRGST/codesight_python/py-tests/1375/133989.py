x=input()
x=x.lower()
sw=0
for i in range(len(x)-2):
	if x[i]=='o' and x[i+1]=='r' and x[i+2]=='o':
		print(i,i+2)
		sw=1
if sw==0:
	print(-1)