x=int(input())
for i in range(x):
    num=int(input())
    p=1
    sw=False
    nuevonum=0
    while num>0:
        dig=num%10
        if dig==2 or dig==3 or dig==5 or dig==7:
            nuevonum = nuevonum +p*dig
            p = p*10
            sw = True
        num = num//10
    if sw:
        print(nuevonum)
    else:
        print(-1)