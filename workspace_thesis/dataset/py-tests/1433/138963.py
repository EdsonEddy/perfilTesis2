a,b=map(int, input().split())
cp=0
for i in range (a,b+1):
	cd=0
	for j in range (1,i+1):
		if i%j==0:
			cd +=1
	if cd ==2:
		cp+=1
print(cp)
