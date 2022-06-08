n = int(input())
for i in range(n):
    cad1= input()
    cad2= input()
    v = []
    pasos = 0
    for j in range(260):
        v.append(0)
    for j in range(len(cad1)):
        v[ord(cad1[j])] = j
    for j in range(1, len(cad2)):
        aux = abs(v[ord(cad2[j])] - v[ord(cad2[j-1])])
        pasos=pasos+aux
    print(pasos)
        