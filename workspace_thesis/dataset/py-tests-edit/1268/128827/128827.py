while True:
       cabezas, patas = map(int, input().split())
       if(patas == 0 and cabezas == 0):
              break
       else:  
              if(patas % 2 == 1):
                     print("-1")
              else:
                     
                     vacas = int(patas/2 - cabezas)
                     gallinas = int(cabezas - vacas)
                     if( vacas < 0 or gallinas < 0):
                            print("-1")
                     else:
                            print(gallinas, vacas)