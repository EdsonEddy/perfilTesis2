n=int(input())
for x in range(0,n):
    c,sw = 0,0
    b = int(input())
    b = (str(bin(b))[2:])
    for i in b:
        if i == '1' and sw==0:
            sw=1
            continue
        elif sw==1:
            if i=='1':
                c=c+1
                sw=0
            else:
                sw=0
    print(c)