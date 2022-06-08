n=int(input())

while n>0:
    x=int(input())
    a=0
    while x>=96:
        num=x%100
        x=x//10
        if num==96:
            a=1
            break
    if a==1:
        print("APLAZADO!")
    else:
        print("TE SALVAS :D")
    n-=1