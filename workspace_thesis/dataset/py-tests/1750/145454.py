from sys import stdin
for cad in stdin:
    cad = cad.split('\n')
    cad = cad[0]
    tam=len(cad)//2
    a=cad[:(tam)]
    b=cad[(tam):]
    if a == b:
        print("si")
    else:
        print("no")