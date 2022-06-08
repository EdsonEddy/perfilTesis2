from sys import *
x=stdin.readline()
y=stdin.readline()	
y=int(y)
s=0
for i in range(y):
    a=stdin.readline()
    s+=int(a)
#toma \n como tamaño de la cadena
x=x[:len(x)-1]
tam=len(x)
s=s%tam
aux = x[:tam-s]
x = x[tam-s:]
stdout.write(x+aux)
