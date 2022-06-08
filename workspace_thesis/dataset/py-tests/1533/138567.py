import sys
for x in sys.stdin:
	n, a = map(int,x.split())
	if(n%2==0):
		if(a>(n//2)):
			print(2*(a-(n//2)))
		else:
			print(1+((a-1)*2))
	elif(a>(n//2)+1):
		print(2*(a-((n//2)+1)))
	else:
		print(1+(2*(a-1)))
