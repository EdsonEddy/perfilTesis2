def serie1(n):
	c,b=1,0
	for j in range(n):
		s1=c+b
		c+=1
		b=s1
		v.append(s1)
def sprimo(n):
	i=2
	while n>0:
		if esprimo(i)=='true':
			n-=1
			w.append(i)
		i+=1
def esprimo(p):
	for l in range(2,p,1):
		if p%l==0:
			t='false'
			break
	else:
		t='true'
	return(t)
			
v=[]
w=[]	
n=int(input())
serie1(n)
sprimo(n)
for p in range(n):
	if p%2 !=0:
		r=str(w[p])+'/'+str(v[p])
		print(r)
	else:
		r=str(v[p])+'/'+str(w[p])
		print(r)
