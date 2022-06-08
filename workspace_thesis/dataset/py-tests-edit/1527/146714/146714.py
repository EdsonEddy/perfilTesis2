n=int(input())
for i in range (n):
    a=int(input())
    sw=0
    while a>9:
        if a%100==96:
            sw=1
        a=a//10
    if sw==1:
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")