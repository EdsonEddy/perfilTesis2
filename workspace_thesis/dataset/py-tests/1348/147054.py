esp=['dek','unu','du','tri','kvar','Kvin','ses','Sep','OK','Nau' ] #define el vector
while True:  #n veces
    num=int(input()) #entrada
    ld, lu =[],[] #????
    dec, u= num//10,num%10 #?? reparte el valor??? a dec,u
    if dec==1:  # si dec es 
        ld.append(esp[0])
    elif dec>1:
        ld.append(esp[dec])
        ld.append(esp[0])
    lu.append(esp[u])
    if u==0:
        print(*ld, sep='') #sep???googlearlo
    elif dec==0:
        print(*lu, sep= '')
    else:
        print(*ld, sep= '', end= ' ')
        print(*lu, sep= '')