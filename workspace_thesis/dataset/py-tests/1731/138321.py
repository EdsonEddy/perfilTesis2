from sys import *
for line in stdin:
	a,b=map(int,line.split())
	if a==0 and b==0:
		print("origen")
	elif a>0 and b>0:
		print("primer cuadrante")
	elif a<0 and b>0:
		print("segundo cuadrante")
	elif a<0 and b<0:
		print("tercer cuadrante")
	elif a>0 and b<0:
		print("cuarto cuadrante")
	elif a==0 and b<0:
		print("eje de ordenadas negativas")
	elif a==0 and b>0:
		print("eje de ordenadas positivas")
	elif a>0 and b==0:
		print("eje de abscisas positivas")
	elif a<0 and b==0:
		print("eje de abscisas negativas")