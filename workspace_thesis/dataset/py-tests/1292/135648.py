while 1:
	m=int(input())
	if m != 0:
		n=input().split()
		s=0
		for i in range(m):
			s+=int(n[i])
		print(s)
	else:
		break