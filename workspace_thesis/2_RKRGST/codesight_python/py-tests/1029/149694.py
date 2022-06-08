def insort(lista,n):
    for i in range(1, n):
        val = lista[i]
        j = i
        while j > 0 and lista[j-1] > val:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = val
while True:
	n=list(map(int,input().split()))
	if len(n)!=0:
		a=0
		b=0
		insort(n,len(n))
		n.reverse()
		for i in range(len (n)):
			if i%2==0:
				a+=n[i]
			else:
				b+=n[i]
		r=a-b
		if r<0:
			r=r*(-1)
			print(r)
		else:
			print(r)
	else:
		break