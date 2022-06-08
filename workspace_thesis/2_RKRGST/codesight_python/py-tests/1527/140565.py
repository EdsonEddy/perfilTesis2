a = int(input())
for i in range (a):
    n = int(input())
    s = 1
    while n  > 0:
        if n % 100 == 96:
            s = 0
            break                                                                                              
        n//=10
    if s == 1:
        print("TE SALVAS :D")
    else:
        print("APLAZADO!")
