while True:
       e = int(input())
       if(e == -1):
              break
       else:
              i = 0
              r = -1
              while(i <= e):
                     r = r + 2
                     i = i + 1
              print(r)
