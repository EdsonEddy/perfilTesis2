a = int(input())
while(a >= 1):
      b = int(input())
      suma = 0
      s = 0
      for x in map(int, input().split()):
            s = x * 2
            if(s % 3 == 0):
                  suma = suma + s
      print("La suma es", suma)
      a = a - 1