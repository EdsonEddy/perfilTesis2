def cad(b):
	b=str(b)
	if (b=="u" or b=="o" or b=="i" or b=="e" or b=="a" or b=="y"):
		b=int(1)
	else:
		b=int(0)
	return b
l=str(input())
l=l.lower()
n=int(len(l))
c=0
ll=str("")
while(c<n):
	sw=int(cad(l[c]))
	if sw==0:
		ll=ll+"."+l[c]
	c=c+1
print(ll)