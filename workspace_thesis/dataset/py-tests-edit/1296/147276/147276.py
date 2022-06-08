casos=int (input())
lista=[]
for i in range(casos):
    def invertir (x):
        new=""
        for j in x:
            new=j+new
        return new
    x=input()
    lista.append(invertir(x))
for k in range (len(lista)-1,-1,-1):
    print (lista[k])