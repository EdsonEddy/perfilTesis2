def Recorredor(k,letra):
    lista='abcdefghijklmnopqrstuvwxyz'
    if letra in lista:
        for j in range (0,len(lista)):
            if letra==lista[j]:
                h=int(j)+int(k)
                if h > int(len(lista))-1:
                     h=h%26
                     letra=lista[h]
                     break
                else:
                     letra=lista[h]
                     break
        return letra
    elif letra=='_':
        letra=' '
        return letra
    else:
        return letra

while True:
    try:
        k,cad=map(str,input().split())
        nuevaPalabra=''
        if int(k)>0 and 1 <= len(cad) <=50:
            if ' ' not in cad:
               for i in range (0,len(cad)):
                     nuevaPalabra=nuevaPalabra+Recorredor(k,cad[i])
               print(nuevaPalabra.upper())
    except ValueError:
        break