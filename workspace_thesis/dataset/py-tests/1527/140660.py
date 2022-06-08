t=int(input())
for i in range(t):
    n=int(input())
    sw=1
    while n>0:
        if n%100==96:
            sw=0
            break
        n//=10
    if sw==1:
        print("TE SALVAS :D")
    else:
         print("APLAZADO!")
