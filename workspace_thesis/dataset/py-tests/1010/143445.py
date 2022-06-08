
n = int(input())
for i in range(n):
    cad = input()
    v = [0 for x in range(260)]
    aux = "ICPCUMSA"
    flag = True
    for j in range(len(cad)):
        v[ ord(cad[j]) ]+=1
    for j in range(len(aux)):
        v[ ord(aux[j]) ]-=1
        if(v[ord(aux[j])] < 0):
            flag = False
    if(flag == True):
        print("ES POSIBLE")
    else:
        print("NO ES POSIBLE")