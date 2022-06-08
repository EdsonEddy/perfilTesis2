while True :
      tu,t = map(int,input().split())
      c = 0
      if t == tu :
            print(1)
      else:
            while t > tu :
                  tu = tu * 2
                  if tu * 2:
                        c = c + 1
            print(c)