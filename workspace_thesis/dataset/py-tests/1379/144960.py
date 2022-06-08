while 1>0:
	n=int(input())
	l=input().split()
	l=sorted(l)

	s=''

	l=l[::-1]

	for i in l:
	
		s=s+i

	print(s)