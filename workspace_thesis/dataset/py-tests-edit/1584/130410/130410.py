while 1:
	n=int(input())
	a=input().split()
	max=int(a[0])
	min=int(a[0])
	for i in range(n-1):
		if int(a[i+1])>max:
			max=int(a[i+1])
		if int(a[i+1])<min:
			min=int(a[i+1])		
	print(max-min)