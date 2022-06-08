from sys import stdin, stdout
for n in stdin:
    n = int(n)
    horas = n//3600
    n%=3600
    minutos = n//60
    n%=60
    stdout.write(str(horas)+" "+str(minutos)+" "+str(n)+"\n")