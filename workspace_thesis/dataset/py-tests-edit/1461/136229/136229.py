n = int(input())
i = 1
while (i <= n):
    a = 0
    x = int(input())
    while (x > 0):
        dig = x % 10
        x = x // 10
        a = a + dig*dig
        #print (a)
        if (x == 0):
            if(a == 1):
                print ("Feliz")
                break
            else:
                if (a == 16):
                    print ("Triste")
                else:
                    x = a
                    a = 0
    i = i + 1