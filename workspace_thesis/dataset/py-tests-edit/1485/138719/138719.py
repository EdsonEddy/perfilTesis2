while True:
	n=int(input())
	a=0
	for i in range(n):
	    numero = input()
	    lista = list(numero)
	    listaReverse=[lista[i-1] for i in range(len(lista),0,-1)]
	    if lista == listaReverse:
	        a+=1
	print(a)