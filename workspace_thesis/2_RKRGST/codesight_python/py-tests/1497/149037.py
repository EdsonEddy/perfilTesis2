def str2bits(codificar=''): #de string a bit 
    return [bin(ord(Y))[2:].zfill(8) for Y in codificar]
codificar=str(input())
b=str2bits(codificar)
for Y in b:
    print (Y,end='')