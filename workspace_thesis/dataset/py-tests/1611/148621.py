def buscando(x,y,v):
	sw=0
	for i in range (x+1):
		if x==i:
			if v[i]==y:
				s=1
				sw=1
			else:
				s=0
	return(s,sw)
def verificar(v,a,b):
	c=0
	for i in range (a):
		if v[i]!=b and c==0:
			sw=2
		if v[i]==b:
			sw=1
			c=1
	return(sw)

a,b=map(int,input().split())
v=list(map(int,input().split()))
s=0
for i in range (a):
	if v[0] == 0:
		print("NO")
		break
	(s,sw)=buscando(v[i],b,v)
	if sw==1:
		if s==0:
			print("NO")
			break
		if s==1:
			print("SI")
			break
	sw=verificar(v,a,b)
	if sw==2:
		print("NO")
		break