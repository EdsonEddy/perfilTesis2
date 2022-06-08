s=str(input())
r=[]
for a in range(0,len(s),1):
	r.append(s[a:])
r.sort()
for a in r:
	print(a)