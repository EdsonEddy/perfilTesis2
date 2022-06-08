s=input()
l=[]
for i in range (len(s)):
	l.append(s[i:])
P=sorted(l)
for j in P:
	print(j)