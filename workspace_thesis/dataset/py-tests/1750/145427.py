from sys import stdin
for cad in stdin:
    cad = cad.split('\n')
    cad = cad[0]
    a = 0
    b = len(cad)-1
    aux1 = ""
    aux2 = ""
    flag = False
    while(a<=b):
        aux1+=cad[a]
        aux2=cad[b]+aux2
        if(aux1 == aux2):
            flag = True
        a+=1
        b-=1
    if(flag == True):
        print("si")
    else:
        print("no")