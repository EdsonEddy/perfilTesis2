n = int(input())
aux = "ICPCUMSA"
for i in range(n):
    v = [0 for x in range(250)]
    flag = True
    cad = input()
    for j in range(len(cad)):
        v[ord(cad[j])]+=1
    for j in range(len(aux)):
        v[ord(aux[j])]-=1
        if(v[ord(aux[j])] < 0):
            flag = False
    if(flag == False):
        print("NO ES POSIBLE")
    else:
        print("ES POSIBLE")
    
