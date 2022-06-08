cas=int(input())
while cas!=0:
	x=(input().split())
	while x!="":
		s=0
		for i in x:
			s=int(i)+s
		print(s)
		cas=int(input())
		if cas==0:
			break
		x=(input().split())