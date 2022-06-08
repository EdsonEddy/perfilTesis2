x=int(input())
if x==0:
	print("error")
else:
	for i in range(x):
		print(2**(2**i)+1,end="")
		if i+1!=x:
			print(end=" ")