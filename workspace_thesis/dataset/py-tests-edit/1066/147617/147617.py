from sys import *
t = int(stdin.readline())
m,l,n,c = 0,0,0,0
for i in range(t):
    cad = stdin.readline().split("\n")
    cad = cad[0]
    m,l,n,c = 0,0,0,0
    for j in range(len(cad)):
        if ord(cad[j])>=97 and ord(cad[j])<=122:
            m=1
        if ord(cad[j])>=65 and ord(cad[j])<=90:
            l=1
        if ord(cad[j])>=48 and ord(cad[j])<=57:
            n=1
        if ord(cad[j])>=33 and ord(cad[j])<=47 or ord(cad[j])>=58 and ord(cad[j])<=64 or ord(cad[j])>=91 and ord(cad[j])<=96 or ord(cad[j])>=123 and ord(cad[j])<=255:
            c=1
    if m==1 and l==1 and n==1 and c==1:
        print("Dale no te jackiaran esta vez.")
    else:
        print("No va dar Botas.")

