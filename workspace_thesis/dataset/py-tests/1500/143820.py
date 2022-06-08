n=int(input())
l=input().split()
nl=[ ]
if n==len(l):
	for j in range(len(l)-1,-1,-1):
		nl.append(l[j])
	for k in range(n):
		if l[k] != nl[k]:
			r='NO'
			break
		else:
			r='SI'
	print(r)