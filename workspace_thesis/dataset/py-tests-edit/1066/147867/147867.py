from sys import *
t=int(stdin.readline())
for i in range(t):
    cad=str(stdin.readline().split("\n"))
    suma=0
    for j in range(len(cad)):
        if(65<=ord(cad[j]) and ord(cad[j])<=90):
            suma=suma+1
            break
    for j in range(len(cad)):
        if (97<=ord(cad[j]) and ord(cad[j])<=122):
            suma=suma+1
            break
    for j in range(len(cad)):
        if (48<=ord(cad[j]) and ord(cad[j])<=57):
            suma=suma+1
            break
    for j in range(len(cad)):
        if (cad[j]=="." or cad[j]=="@" or cad[j]=="-" or cad[j]=="_" or cad[j]==">" or cad[j]=="<"):
            suma=suma+1
            break
    if(suma==4):
        print("Dale no te jackiaran esta vez.")
    else:
        print("No va dar Botas.")