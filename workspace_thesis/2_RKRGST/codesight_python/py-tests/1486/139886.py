from sys import stdin
def serie(n):
	a=1
	b=0
	t=1
	for i in range(1,n+1):
		
		if(i%2==0):
			par=2*t
			t=t+1
			print(par)
		else:
			c=a+b
			a=b
			b=c
			print(c)
			
for n in stdin:
	n=int(n)
	serie(n)