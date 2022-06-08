l=["unu", "du", "tri", "kvar", "Kvin", "ses", "Sep", "OK", "Nau", "dek"]
while 1>0:
    n=int(input())
    if n<=10:
        print(l[n-1])
    elif n<20:
        print(l[9],l[n%10-1])
    elif n%10==0:
        print(l[n//10-1],end="")
        print(l[9])
    else:
        print(l[n // 10-1], end="")
        print(l[9],l[n%10-1])
