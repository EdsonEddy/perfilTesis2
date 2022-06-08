import sys
for linea in sys.stdin:
    if linea == "\n":
        break
    datos = list(map(int,linea.split()))
    print(sum(datos[0:]))
