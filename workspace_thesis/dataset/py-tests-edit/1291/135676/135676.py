while True:
	l=list(map(int,input().split()))
	if len(l)==0:
		break
	else:
		print(sum(l))