import sys
v = [" " ,"unu" , "du", "tri", "kvar", "Kvin", "ses", "Sep", "OK", "Nau", "dek"]
for n in sys.stdin:
    n = int(n)
    if 0 <= n <= 10:
        num = v[n]
        print(num)
    else:
        n =str(n)
        uni=int(n[1])
        dec=int(n[0])
        if 11<=int(n)<=19:
            num = "dek", v[uni]
            print(*num)
        if 20<=int(n)<=99:
            dec = v[dec]+"dek"
            if uni == 0:
                print(dec)
            else:
                uni = v[uni]
                num = dec,uni
                print(*num)



