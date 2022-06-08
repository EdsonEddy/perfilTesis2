while True:
	X=int(input())
	if X==0:
		break
	else:
		l=list(map(int,input().split()))
		print(sum(l))