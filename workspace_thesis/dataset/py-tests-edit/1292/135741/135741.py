from sys import stdin
for n in stdin:
	if n==0:
		break
	m=int(n)
	s=0
	if m==0:
		break
	else:
		a=input().split()
		for j in range(m):
			s = s+int(a[j])
	print(s)