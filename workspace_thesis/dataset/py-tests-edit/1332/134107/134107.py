a=input()
l=['a','e','i','o','u','y']
a=a.lower()
for i in range(6):
	j=0
	while j <len(a):
		if l[i]==a[j]:
			if j==len(a)-1:
				a=a[:j]
			else:
				a=a[:j]+a[j+1:]
		else:
			j+=1
		
a='.'+a
l=len(a)
j=2
for k in range (l):
	a=a[:k+j]+'.'+a[k+j:]
	j+=1	
l=len(a)
a=a[:l-2]
print(a)