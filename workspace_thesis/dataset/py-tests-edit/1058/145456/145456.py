a = int(input())
while(a != 0):
      b = int(input())
      lista = []
      for x in map(int, input().split()):
            lista.append(x)
      for h in range(1, len(lista)):
            for k in range(0, len(lista) - h):
                  if(lista[k] > lista[k + 1]):
                        aux = lista[k]
                        lista[k] = lista[k+1]
                        lista[k + 1] = aux
      d = ''
      f = " "
      for e in lista:
            
            if((lista[len(lista)-1]) == e):
                  e = str(e)
                  d = d + e  
            else:
                  e = str(e)
                  d = d + e
                  d = d + f
      print(d)
      a = a - 1