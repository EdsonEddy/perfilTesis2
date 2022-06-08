s=input()
k=[]
for i in range (len(s)):
	k.append(s[i:])
f=sorted(k)
for u in f:
	print(u)
