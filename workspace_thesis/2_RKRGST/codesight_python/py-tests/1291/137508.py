x=(input().split())
while x!=[]:
	s=0
	for i in x:
		s=int(i)+s
	print(s)
	x=(input().split())