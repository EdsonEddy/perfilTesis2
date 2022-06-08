month = list(map(int, input().rstrip().split()))
mayor = max(month)
indice = (month.index(mayor)+1)
if indice == 1:
	print("Escala la primera")
if indice == 2:
	print("Escala la segunda")
if indice == 3:
	print("Escala la tercera")
