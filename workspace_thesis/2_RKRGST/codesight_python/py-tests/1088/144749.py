import math
n=int(input())
for i in range(n):
    teclado=input()
    palabra=input()
    v=[]
    pasos=0
    for j in range(260):
        v.append(0)
    for j in range(len(teclado)):
        v[ord(teclado[j])]=j
    for j in range(1,len(palabra)):
        aux=abs(v[ord(palabra[j])]-v[ord(palabra[j-1])])
        pasos=pasos+aux
    print(pasos)
