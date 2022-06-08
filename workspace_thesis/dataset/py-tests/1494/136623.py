def fibo(x):
    fib=[]
    a, b = 0, 1
    for i in range(x):
        a, b = b,b+a
        fib.append(a)
    return(fib)
   
def prim(y):
	pri = []
	for i in range(2,1000):
		for j in range(2,i):
			if i%j ==0:
				break
		else:
			pri.append(i)
		if len(pri) == y:
			return(pri)
while True:
	y,x = map(int,input().split())
	f, p, s = fibo(y), prim(y),0
	s = float(s)
	for i in range(0, y):
		o = f[i]/(p[i]*x)
		s += o
	print('{:.2f}'.format(s))