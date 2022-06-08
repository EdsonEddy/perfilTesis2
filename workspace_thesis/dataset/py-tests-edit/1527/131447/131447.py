a=int(input())
i=1
while (i<=a):
    d = int(input())
    e = 0
    t = 0
    if (d >= 100):
        while (d > 0):
            dig = d % 10
            d = d // 10
            if (e <= 1):
                t = t + (dig*10**e)
                if (e == 1):
                    
                    if (t == 96):
                        print ("APLAZADO!")
                        d = 0
                    else:
                        t = dig
                        if (d == 0):
                            print ("TE SALVAS :D")
                        else:
                            t = dig
                else:
                    e = e + 1            
    i = i + 1