l=input()
f=input()
ln=len(f)
c=0
f=f.lower()
for i in range(ln):
	if l==f[i]:
		c+=1
print(c)