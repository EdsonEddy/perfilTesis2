while True:
       n = int(input())
       nn = 0
       cd = 0
       while (n != 0):
              d = n % 10
              n = n // 10
              nn = nn * 10 + d
       cc = 0
       sp = 0
       si = 0
       while (nn != 0):
              dd = nn % 10
              nn = nn // 10
              if (cc % 2 == 0):
                     sp = sp + dd
                     cc = cc + 1
              else:
                     si = si + dd
                     cc = cc + 1
       if (sp == si):
              print("SI")
       else:
              print("NO")