n = int(input())
c = 0
while(n > c):
       nn = int(input())
       if(nn == 0):
              print("1")
       elif(nn == 1):
              print("0")
       elif(nn % 2 == 0):
              nn = nn // 2
              ee = 0
              i = 0
              while(nn > i):
                     ee = ee * 10 + 8
                     i = i + 1
              print(ee)
       elif(nn % 2 == 1):
              nn = nn // 2
              dd = 4
              j = 0
              while(nn > j):
                     dd = dd * 10 + 8
                     j = j + 1
              print(dd)
       c = c + 1