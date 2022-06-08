n=int(input())
if n>=0 and n<=10000:
	n=n/240
	lb=int(n)
	n=n-lb
	n=n*20
	ch=int(n)
	n=n-ch
	pn=round(n*12)	
r='('+str(lb)+', '+str(ch)+', '+str(pn)+')'
print(r)
	