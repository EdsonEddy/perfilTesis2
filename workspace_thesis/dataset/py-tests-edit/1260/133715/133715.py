n=int(input())
for j in range(n):
	a,b=map(int,input().split())
	if a<b:
		min=a
	else:
		min=b
	for i in range(min,0,-1):
		if a%i == 0 and b%i ==0:
			print(i)
			break