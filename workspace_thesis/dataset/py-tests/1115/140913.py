n=input()
st=0
s=0
c=0
for j in n:
	st += int(j)
for i in range(len(n)-1):
	s+=int(n[i])
	if s%3==0 and (st-s)%3==0:
		c+=1
		
print(c)