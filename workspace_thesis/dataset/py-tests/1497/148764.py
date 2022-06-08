a = input()
acu = ''
numeros = ['0','1','2','3','4','5','6','7','8','9']
lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lis = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
listas = ['97','98','99','100','101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122']
for letra in (a):
    if (str(letra) == str(' ')):
            e = bin(32)
            e = e.replace('b','0')
            acu = str(acu) + str(e)
    for b in range (26):
        if (str(letra) == str(lista[b])):
            e = bin(int(listas[b]))
            e = e.replace('b','')
            acu = str(acu) + str(e)
            break
    for c in range(26):
        if (str(letra) == str(lis[c])):
            e = bin(int(listas[c]) - 32)
            e = e.replace('b','') 
            acu = str(acu) + str(e)
        
            break
    for d in range (10):
        if (str(letra) == str(numeros[d])):
            e = bin(int(listas[d]) - 49)
            e = e.replace('b','0')
            acu = str(acu) + str(e)
print (acu)