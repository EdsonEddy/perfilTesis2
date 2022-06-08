n=int(input())
for i in range(1,n+1):
	a,b,c=map(int,input().split())
	if b>a and b<c:
		print('Case',str(i)+':',b)
	elif a>b and a<c:
		print('Case',str(i)+':',a)
	elif c>a and c<b:
		print('Case',str(i)+':',c)
	elif b>c and b<a:
		print('Case',str(i)+':',b)
	elif c>b and c<a:
		print('Case',str(i)+':',c)
	elif a>b and a<c:
		print('Case',str(i)+':',a)
	else:
		print('Case',str(i)+':',a) 