n=int(input())
for i in range(n):
	d=int(input())
	s=list(input().split())
	r=[]
	for a in s:
		r.append(int(a))
	r.sort()
	print(*r)