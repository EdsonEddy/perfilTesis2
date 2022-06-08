s=str(input())
l=[]
for i in range(len(s)):
	l.append(s[i:])
l=sorted(l)
for i in l:
	print(i)