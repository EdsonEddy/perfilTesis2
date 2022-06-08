c,n=input().split()
e=len(c)
n=int(n)
p=e-n
if n<=e:
	nc=c[p:]
	r=nc+c[:p]
	print(r)