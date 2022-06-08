n=int(input())
for i in range(n):
	a,b=map(int,input().split())
	s=tuple(input().split())
	r=0
	for j in range(a,b+1,1):
		r+=int(s[j])
	print(r)