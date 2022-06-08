while True:
       n = int(input())
       a = 0
       b = 1
       c = 0
       f = 0
       while(n != c):
              f = a + b
              b = a
              a = f
              c = c + 1
       print(f)