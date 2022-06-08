#se paso con su examen Msc.TERAN  
def str2bits(s=''): #de string a bit 
    return [bin(ord(x))[2:].zfill(8) for x in s]
s=str(input())
b=str2bits(s)
for x in b:
    print (x,end='') 
#la otra def era para ver si al convertir de bianrio a cadena me pediria el 0b y tendria q rehacer