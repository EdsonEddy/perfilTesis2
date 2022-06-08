while True:
	n=int(input())
	k=0
	d=(2**k)-1
	while d<n:
		k+=1
		d=(2**k)-1
	print(k)