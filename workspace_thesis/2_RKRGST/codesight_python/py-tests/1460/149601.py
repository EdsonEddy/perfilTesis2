n=int(input())
au=1
for i in range(n):
	if i!=0:
		print("")
	for j in range(n):
		if j>i and j<(n-i)-1 or j<i and j>(n-i)-1:
			print("0",end="")
		else:
			if i==n-1 and j==n-1:
				print("1")
			else:
				print("1",end="")