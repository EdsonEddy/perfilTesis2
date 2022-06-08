from sys import stdin
for i in stdin:
	a=i.split()
	s=0
	for j in range(len(a)):
		if int(a[j])==0:
			break
		else:
			s = s+int(a[j])
	print(s)