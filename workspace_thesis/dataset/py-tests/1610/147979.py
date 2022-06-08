n=str(input())
c=0
x=""
for i in range (len(n)):
	if n[i]=="1":
		c=c+1
	if n[i] =="0":
		x=x+str(c)
		c=0
x=x+str(c)
print(x)