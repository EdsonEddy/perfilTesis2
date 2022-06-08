while True:
	entrada=str(input())
	d=[]
	for i in entrada:
		d.append(i)
	g=sorted(d)
	p=''
	for y in g:
		p=p+y
	diccionario={}
	for letra in p:
	    if letra in diccionario:
	        diccionario[letra]=diccionario[letra]+1
	    else:
	        diccionario[letra]=1
	 
	for i in diccionario:
		valor = diccionario.get(i)
		print('{}={}'.format(i,valor))
	print('')