#se paso con su examen Msc.TERAN  
def str2bits(s=''): #de string a bit 
    return [bin(ord(x))[2:].zfill(8) for x in s]
def bits2str(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
s=str(input())
b=str2bits(s)
s2=bits2str(b)
for x in b:
    print (x,end='')