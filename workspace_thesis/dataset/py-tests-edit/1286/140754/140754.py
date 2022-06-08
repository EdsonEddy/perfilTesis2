t = int(input())
while(t):
	t -= 1
	ans = 0
	A = []	
	while(1):
		A += [int(i) for i in input().split()]	
		if(A[-1]==0):break
	i = 1 
	while(i<len(A)):
		if(A[i]>A[i-1]):
			ans += 1
		i += 1
	print(ans)
	