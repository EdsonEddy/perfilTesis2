a = int(input())
lista = [2, 3, 5, 7]
while(a != 0):
      b = int(input())
      nn = 0
      potencia = 1
      while(b != 0):
            dig = b % 10
            b = b // 10
            if(dig in lista):
                  nn = nn + dig * potencia
                  potencia = potencia * 10
      if(nn != 0):
            print(nn)
      else:
            print("-1")    
      a = a - 1