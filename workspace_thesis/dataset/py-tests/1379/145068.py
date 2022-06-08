while True:
	n=int(input())
	if n!=0:
		lis=list(map(str,input().split()))
		lis.sort(reverse=True)
		print(*lis,sep="")
	else:
		break