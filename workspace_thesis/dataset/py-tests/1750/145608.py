from sys import stdin
for palabra in stdin:
    palabra = palabra.split('\n')
    palabra = "".join(palabra)
    n = len(palabra)
    m = n // 2
    cont = 1
    sw = False
    while (cont <= m):
        if (palabra[0:cont:] == palabra[n-cont:n:]):
           sw = True
        cont = cont + 1
    if sw == True:
        print("si")
    else:
        print("no")