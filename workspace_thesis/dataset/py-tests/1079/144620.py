from sys import stdin
for cad in stdin:
    cad,buff = map(str,cad.split("\n"))
    if(cad == "end"):
        break
    n = len(cad)
    aux = cad
    cad = cad + "***"
    flag = False
    vocales = 0
    consonantes = 0
    for i in range(n):
        if(cad[i] == 'a' or cad[i] == 'e' or cad[i] == 'i' or cad[i] == 'o' or cad[i] == 'u'):
            flag = True
            vocales+=1
            consonantes = 0
        else:
            vocales = 0
            consonantes+=1
        if(vocales >= 3 or consonantes >= 3):
            flag = False
            break
        if( (cad[i] != 'e' and cad[i] != 'o') and cad[i] == cad[i+1] ):
            flag = False
            break
    if(flag == True):
        print("<"+aux+"> is acceptable.")
    else:
        print("<"+aux+"> is not acceptable.")
        
        
